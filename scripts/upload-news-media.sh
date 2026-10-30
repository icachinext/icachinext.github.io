#!/usr/bin/env bash
# Upload docs/public/news/* to the public R2 bucket.
# Objects are served at https://media.icachi.org/news/<filename>
set -euo pipefail

bucket="icachi-media"
dir="docs/public/news"

if [[ ! -d "$dir" ]]; then
  echo "Missing $dir" >&2
  exit 1
fi

shopt -s nullglob
files=("$dir"/*)
if [[ ${#files[@]} -eq 0 ]]; then
  echo "No files in $dir" >&2
  exit 1
fi

for file in "${files[@]}"; do
  [[ -f "$file" ]] || continue
  name="$(basename "$file")"
  ext="${name##*.}"
  case "$ext" in
    jpg|jpeg) content_type="image/jpeg" ;;
    png) content_type="image/png" ;;
    webp) content_type="image/webp" ;;
    gif) content_type="image/gif" ;;
    svg) content_type="image/svg+xml" ;;
    *)
      echo "Skip $name (unknown type)" >&2
      continue
      ;;
  esac

  echo "Put news/$name"
  npx --yes wrangler@4 r2 object put "$bucket/news/$name" \
    --file "$file" \
    --content-type "$content_type" \
    --remote
done
