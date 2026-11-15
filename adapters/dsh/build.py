#!/usr/bin/env python3
"""Pack the PMO source as a local DeepSeek Harness plugin."""

import argparse
import json
import re
import shutil
import tarfile
from pathlib import Path
from tempfile import TemporaryDirectory


ADAPTER = Path(__file__).resolve().parent
SKILL = ADAPTER.parents[1] / "package" / "skills" / "pmo"
SKILL_NAME = "pmo-dsh"


def pack(output):
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((ADAPTER / "package.json").read_text(encoding="utf-8"))
    destination = output / f"{manifest['name']}-{manifest['version']}.tgz"

    with TemporaryDirectory(prefix="pmo-dsh-", dir=output) as staging:
        package = Path(staging) / "package"
        skill_directory = package / "skills" / SKILL_NAME
        shutil.copytree(SKILL, skill_directory, ignore=shutil.ignore_patterns(".DS_Store"))

        entry = skill_directory / "SKILL.md"
        opening, frontmatter, body = entry.read_text(encoding="utf-8").split("---\n", 2)
        frontmatter, changed = re.subn(r"^name: pmo$", f"name: {SKILL_NAME}", frontmatter, flags=re.M)
        description = re.search(r"^description: ([^\n]+)$", frontmatter, flags=re.M)
        if opening or changed != 1 or not description:
            raise ValueError("PMO 技能入口须有 name: pmo 和单行 description")
        entry.write_text(f"---\n{frontmatter}---\n{body}", encoding="utf-8")

        manifest["description"] = description[1]
        (package / "package.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        for filename in ("cordis.patch.yml", "index.js"):
            shutil.copyfile(ADAPTER / filename, package / filename)

        archive = Path(staging) / destination.name
        with tarfile.open(archive, "w:gz") as tar:
            tar.add(package, arcname="package")
        archive.replace(destination)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", type=Path, default=ADAPTER / "dist", help="插件包输出目录")
    args = parser.parse_args()
    try:
        print(pack(args.output))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
