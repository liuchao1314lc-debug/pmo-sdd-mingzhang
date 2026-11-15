#!/usr/bin/env python3
"""Build the PMO skill ZIP for WorkBuddy desktop import."""

import argparse
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile


ADAPTER = Path(__file__).resolve().parent
SKILL = ADAPTER.parents[1] / "package" / "skills" / "pmo"
SKILL_NAME = "pmo-workbuddy"
VERSION = "0.1.0"


def pack(output):
    entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    opening, frontmatter, body = entry.split("---\n", 2)
    frontmatter, changed = re.subn(r"^name: pmo$", f"name: {SKILL_NAME}", frontmatter, flags=re.M)
    if opening or changed != 1:
        raise ValueError("PMO 技能入口应有且仅有一个 name: pmo")

    workbuddy_entry = (
        f"---\n{frontmatter}"
        "display_name: PMO 项目治理\n"
        "display_name_en: PMO project governance\n"
        f"version: {VERSION}\n"
        f"---\n{body}"
    )
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    destination = output / f"{SKILL_NAME}-{VERSION}.zip"
    with TemporaryDirectory(prefix="pmo-workbuddy-", dir=output) as staging:
        archive = Path(staging) / destination.name
        with ZipFile(archive, "w", ZIP_DEFLATED) as package:
            for path in sorted(SKILL.rglob("*")):
                if not path.is_file() or path.name == ".DS_Store":
                    continue
                relative = path.relative_to(SKILL)
                member = f"{SKILL_NAME}/{relative.as_posix()}"
                if relative == Path("SKILL.md"):
                    package.writestr(member, workbuddy_entry)
                else:
                    package.write(path, member)
        archive.replace(destination)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", type=Path, default=ADAPTER / "dist", help="技能包输出目录")
    args = parser.parse_args()
    try:
        print(pack(args.output))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
