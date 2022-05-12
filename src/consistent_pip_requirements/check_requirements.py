from __future__ import annotations

import itertools
import sys
from pathlib import Path


def main(argv=None):

    files = _find_requirements_files()
    if len(files) <= 1:
        return

    requirements_by_file = {path.name: _read_requirements(path) for path in files}

    for file1, file2 in itertools.combinations(path.name for path in files):
        if not _compare_requirements(
            requirements_by_file[file1], requirements_by_file[file2]
        ):
            sys.exit("Mismatched versions found")

    print("Requirements match")


def _find_requirements_files(root: Path | None = None) -> list[Path]:
    """Find requirements files for the project.

    Either returns all `.txt` files in a `requirements` subdirectory
    or any file matching the pattern "*requirements*.txt" in the root.

    """
    root = root or Path(".")
    requirements_dir = root / "requirements"
    if requirements_dir.is_dir():
        return [path for path in requirements_dir.glob("*.txt")]
    return [path for path in root.glob("*requirements*.txt")]


def _read_requirements(filename: Path) -> dict[str, str]:
    """Read dictionary of package versions from requirements file."""

    packages = {}
    with filename.open("r") as f:
        for line in f:
            line = line.strip()
            if line[0] == "#":
                continue
            try:
                package, version = line.split("==", 1)
            except ValueError:
                continue
            packages[package] = version

    return packages


def _compare_requirements(first: dict[str, str], second: dict[str, str]) -> bool:

    overlapping_packages = set(first.keys()).intersection(second.keys())
    no_mismatches = True
    for package in overlapping_packages:
        if first[package] != second[package]:
            print(f"Mismatch for '{package}': {first[package]} != {second[package]}")
            no_mismatches = False
    return no_mismatches


if __name__ == "__main__":
    sys.exit(main())
