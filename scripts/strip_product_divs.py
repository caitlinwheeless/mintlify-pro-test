#!/usr/bin/env python3
"""Strip product-specific div wrappers from MDX files.

For the target product:
  - <div className="<product>-only">...</div> → keep inner content (unwrap)
For the other product:
  - <div className="<other>-only">...</div>   → remove entirely

Handles nested <div> tags correctly.
"""
import argparse
import glob
import re
import sys

PRODUCTS = ('opensource', 'enterprise')

def strip_divs(content: str, keep: str, remove: str) -> str:
    lines = content.split('\n')
    out = []
    skip_depth = 0
    unwrap_depth = 0

    for line in lines:
        stripped = line.strip()

        if skip_depth > 0:
            if re.match(r'<div\b', stripped):
                skip_depth += 1
            elif stripped == '</div>':
                skip_depth -= 1
            continue

        if unwrap_depth > 0:
            if re.match(r'<div\b', stripped):
                unwrap_depth += 1
                out.append(line)
            elif stripped == '</div>':
                unwrap_depth -= 1
                if unwrap_depth > 0:
                    out.append(line)
            else:
                out.append(line)
            continue

        if stripped == f'<div className="{remove}-only">':
            skip_depth = 1
            continue

        if stripped == f'<div className="{keep}-only">':
            unwrap_depth = 1
            continue

        out.append(line)

    result = '\n'.join(out)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('product', choices=PRODUCTS,
                        help='The product to build for (keeps this product\'s content)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would change without writing files')
    args = parser.parse_args()

    keep = args.product
    remove = [p for p in PRODUCTS if p != keep][0]

    files = glob.glob('docs/source/**/*.mdx', recursive=True)
    changed = 0

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()

        result = strip_divs(original, keep, remove)

        if result != original:
            changed += 1
            if args.dry_run:
                print(f'  would update: {filepath}')
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f'  updated: {filepath}')

    print(f'\nTotal files {"that would change" if args.dry_run else "updated"}: {changed}')

if __name__ == '__main__':
    main()
