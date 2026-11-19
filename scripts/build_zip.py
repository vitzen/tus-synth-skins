#!/usr/bin/env python3
"""
Build release zip for Simpless skin.
Usage: python build_zip.py --source-dir Simpless_Xenia --synth xenia --version v0.1.0 --output-dir .
"""
import argparse
import os
import sys
import zipfile
from pathlib import Path


def build_zip(source_dir: str, synth: str, version: str, output_dir: str) -> str:
    src = Path(source_dir)
    if not src.exists():
        sys.exit(f"Source directory not found: {src}")

    # Output zip name: Simpless-Xenia-v0.1.0.zip
    zip_name = f"Simpless-{synth.capitalize()}-{version}.zip"
    zip_path = Path(output_dir) / zip_name

    # Folder inside zip: always "Simpless/"
    root_in_zip = "Simpless"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in src.rglob('*'):
            if file_path.is_file():
                # Skip hidden files and .git
                if any(part.startswith('.') for part in file_path.parts):
                    continue
                # Archive path: Simpless/relative/path
                rel_path = file_path.relative_to(src)
                archive_path = f"{root_in_zip}/{rel_path}"
                zf.write(file_path, archive_path)

    print(f"Created: {zip_path}")
    print(f"Root folder in zip: {root_in_zip}/")
    return str(zip_path)


def main():
    parser = argparse.ArgumentParser(description='Build Simpless skin release zip')
    parser.add_argument('--source-dir', required=True, help='Source directory (e.g., Simpless_Xenia)')
    parser.add_argument('--synth', required=True, help='Synth name (e.g., xenia)')
    parser.add_argument('--version', required=True, help='Version tag (e.g., v0.1.0)')
    parser.add_argument('--output-dir', default='.', help='Output directory for zip')
    args = parser.parse_args()

    zip_path = build_zip(args.source_dir, args.synth, args.version, args.output_dir)
    # Output for GitHub Actions (writes to GITHUB_OUTPUT file if running in Actions)
    github_output = os.environ.get('GITHUB_OUTPUT')
    if github_output:
        with open(github_output, 'a') as f:
            f.write(f"zip_path={zip_path}\n")
    print(f"zip_path={zip_path}")


if __name__ == '__main__':
    main()