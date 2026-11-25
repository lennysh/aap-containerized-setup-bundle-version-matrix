#!/usr/bin/env bash
# Backfill bundle data from the quay.io ORAS repository, one bundle at a time:
# pull -> inspect -> delete, so only one bundle tarball is on disk at any moment.
#
# Requires: oras (logged in: `oras login quay.io`), ansible-playbook, python3, rpm.
#
# Usage: scripts/backfill_oras.sh [--dry-run]
#
# Environment overrides:
#   ORAS_REPO   quay.io/aap/containerized-installer
#   ARCH        x86_64            (aarch64, ppc64le, s390x also published)
#   MIN_AAP     2.5               oldest AAP version to consider
#   SINCE       (unset)           only bundles whose manifest `created` is on/after
#                                 this date, e.g. SINCE=2025-11-24
#   LIMIT       0                 stop after this many bundles inspected (0 = no limit)
#   WORK_DIR    /var/tmp/aap-bundle-backfill
set -uo pipefail

ORAS_REPO=${ORAS_REPO:-quay.io/aap/containerized-installer}
ARCH=${ARCH:-x86_64}
MIN_AAP=${MIN_AAP:-2.5}
SINCE=${SINCE:-}
LIMIT=${LIMIT:-0}
WORK_DIR=${WORK_DIR:-/var/tmp/aap-bundle-backfill}
DRY_RUN=false
[[ ${1:-} == --dry-run ]] && DRY_RUN=true

REPO_ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$REPO_ROOT" || exit 1

log() { printf '%s %s\n' "$(date '+%F %T')" "$*"; }

version_ge() { [[ $(printf '%s\n%s\n' "$2" "$1" | sort -V | head -1) == "$2" ]]; }

manifest_created() {
  oras manifest fetch "$ORAS_REPO:$1" 2>/dev/null |
    python3 -I -c 'import json,sys; print(json.load(sys.stdin).get("annotations",{}).get("org.opencontainers.image.created",""))'
}

log "Listing tags in $ORAS_REPO"
mapfile -t TAGS < <(oras repo tags "$ORAS_REPO" |
  grep -E "^ansible-automation-platform-containerized-setup-bundle-[0-9]+\.[0-9]+-.+-${ARCH}\.tar\.gz$" |
  sort -Vr)
log "Found ${#TAGS[@]} $ARCH bundle tags"

done_list=() failed_list=() count=0
for tag in "${TAGS[@]}"; do
  version=${tag#ansible-automation-platform-containerized-setup-bundle-}
  version=${version%-"$ARCH".tar.gz}
  aap=${version%%-*}
  id="$version-$ARCH"

  version_ge "$aap" "$MIN_AAP" || continue
  if [[ -f bundles/$aap/$id/bundle.yml ]]; then
    continue
  fi
  if [[ -n $SINCE ]]; then
    created=$(manifest_created "$tag")
    if [[ -n $created && ${created:0:10} < $SINCE ]]; then
      log "skip $id (created $created, before $SINCE)"
      continue
    fi
  fi
  if $DRY_RUN; then
    log "would inspect $id"
    continue
  fi
  if (( LIMIT > 0 && count >= LIMIT )); then
    log "LIMIT=$LIMIT reached"
    break
  fi

  dir="$WORK_DIR/$id"
  rm -rf "$dir" && mkdir -p "$dir"
  log "pull $id"
  if ! oras pull --no-tty -o "$dir" "$ORAS_REPO:$tag" >"$dir.pull.log" 2>&1; then
    log "FAILED pull $id (see $dir.pull.log)"
    failed_list+=("$id (pull)")
    rm -rf "$dir"
    continue
  fi
  file=$(find "$dir" -type f -name "$tag" | head -1)
  if [[ -z $file ]]; then
    log "FAILED $id: pulled file not found"
    failed_list+=("$id (missing file)")
    rm -rf "$dir"
    continue
  fi
  log "inspect $id ($(du -h "$file" | cut -f1))"
  if ansible-playbook bundle_inspector.yml -e "bundle_dir=$(dirname "$file")" \
      -e bundle_inspector_generate_markdown=false >"$dir.inspect.log" 2>&1; then
    done_list+=("$id")
    rm -f "$dir.pull.log" "$dir.inspect.log"
  else
    log "FAILED inspect $id (see $dir.inspect.log)"
    failed_list+=("$id (inspect)")
  fi
  rm -rf "$dir"
  count=$((count + 1))
done

if ! $DRY_RUN && (( ${#done_list[@]} > 0 )); then
  log "Regenerating markdown"
  ansible-playbook md_generator.yml >/dev/null || log "FAILED markdown generation"
fi

log "Inspected: ${#done_list[@]}  Failed: ${#failed_list[@]}"
for f in "${failed_list[@]}"; do log "  failed: $f"; done
(( ${#failed_list[@]} == 0 ))
