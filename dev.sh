#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

usage() {
  echo "Usage: ./dev.sh <opensource|enterprise>"
  echo ""
  echo "Copies the selected product's docs.json to the repo root,"
  echo "strips the other product's content divs, and starts mint dev."
  echo "Files are restored to their original state when the server stops."
  exit 1
}

if [[ $# -ne 1 ]]; then
  usage
fi

PRODUCT="$1"

case "$PRODUCT" in
  opensource|enterprise)
    SOURCE="${PRODUCT}/docs.json"
    if [[ ! -f "$SOURCE" ]]; then
      echo "Error: ${SOURCE} not found."
      exit 1
    fi

    echo "Copying ${SOURCE} → docs.json"
    cp "$SOURCE" docs.json

    echo "Stripping product divs for ${PRODUCT}..."
    python3 scripts/strip_product_divs.py "$PRODUCT"

    restore_files() {
      echo ""
      echo "Restoring original files..."
      git checkout -- docs/
      echo "Done."
    }
    trap restore_files EXIT

    echo "Starting mint dev for ${PRODUCT}..."
    npx mintlify dev
    ;;
  *)
    echo "Error: Unknown product '${PRODUCT}'"
    usage
    ;;
esac
