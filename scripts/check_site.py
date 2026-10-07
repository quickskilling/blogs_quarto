#!/usr/bin/env python3
"""Check the portfolio for leftover template content and thin project pages.

Usage:
    uv run python scripts/check_site.py            # report problems, exit 0
    uv run python scripts/check_site.py --strict   # exit 1 if anything is found
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDERS = ["YOUR-USERNAME", "YOUR-PROFILE", "YOUR-REPO", "Your Name", "TODO"]
REQUIRED_PROJECT_FIELDS = ["title", "description", "date", "categories"]
SOURCES = ["_quarto.yml", "index.qmd", "about.qmd", "skills.qmd"]


def frontmatter(path: Path) -> dict:
    m = re.match(r"^---\n(.*?)\n---", path.read_text(), re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def main() -> int:
    problems: list[str] = []

    files = [ROOT / f for f in SOURCES]
    files += sorted(ROOT.glob("projects/*/index.qmd")) + sorted(ROOT.glob("posts/*/index.qmd"))
    for f in files:
        if not f.exists():
            continue
        for n, line in enumerate(f.read_text().splitlines(), 1):
            for p in PLACEHOLDERS:
                if p in line:
                    problems.append(f"{f.relative_to(ROOT)}:{n}: placeholder '{p}'")

    projects = sorted(ROOT.glob("projects/*/index.qmd"))
    real = 0
    for f in projects:
        fm = frontmatter(f)
        rel = f.relative_to(ROOT)
        if fm.get("example"):
            problems.append(f"{rel}: still marked `example: true` (replace or delete this sample)")
            continue
        real += 1
        for field in REQUIRED_PROJECT_FIELDS:
            if not fm.get(field):
                problems.append(f"{rel}: missing frontmatter field '{field}'")
        if not fm.get("repo"):
            problems.append(f"{rel}: no `repo` link (readers want to see the code)")
        words = len(re.sub(r"```.*?```", "", f.read_text(), flags=re.S).split())
        if words < 150:
            problems.append(f"{rel}: only ~{words} words of prose; explain problem, approach, result")
    if real < 3:
        problems.append(f"only {real} real project(s); aim for at least 3")
    if not any(frontmatter(f).get("featured") and not frontmatter(f).get("example") for f in projects):
        problems.append("no real project has `featured: true`, so the home page is empty")

    if problems:
        print(f"{len(problems)} thing(s) to fix:")
        for p in problems:
            print(f"  - {p}")
    else:
        print("All checks passed.")
    return 1 if problems and "--strict" in sys.argv else 0


if __name__ == "__main__":
    sys.exit(main())
