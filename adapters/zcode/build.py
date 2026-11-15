#!/usr/bin/env python3
"""Build an installable local ZCode marketplace containing the PMO plugin."""

import argparse
import json
import re
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


ADAPTER = Path(__file__).resolve().parent
SKILL = ADAPTER.parents[1] / "package" / "skills" / "pmo"
ZCODE_SKILL_NAME = "pmo-zcode"
PLUGIN = Path("plugins/pmo")
MANIFEST = PLUGIN / ".zcode-plugin/plugin.json"
MARKETPLACE = Path("marketplace.json")


def files(directory):
    return {
        path.relative_to(directory): path.read_bytes()
        for path in directory.rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    }


def copy_skill(destination):
    shutil.copytree(SKILL, destination, ignore=shutil.ignore_patterns(".DS_Store"))
    skill_file = destination / "SKILL.md"
    opening, frontmatter, body = skill_file.read_text(encoding="utf-8").split("---\n", 2)
    if opening:
        raise ValueError("技能入口缺少开头的 YAML frontmatter")
    frontmatter, changed = re.subn(r"^name: pmo$", f"name: {ZCODE_SKILL_NAME}", frontmatter, flags=re.MULTILINE)
    if changed != 1:
        raise ValueError("技能入口应有且仅有一个 name: pmo")
    skill_file.write_text(f"---\n{frontmatter}---\n{body}", encoding="utf-8")


def build(output):
    market = json.loads((ADAPTER / MARKETPLACE).read_text(encoding="utf-8"))
    plugin = json.loads((ADAPTER / MANIFEST).read_text(encoding="utf-8"))
    entry, = market["plugins"]
    if entry["source"] != f"./{PLUGIN.as_posix()}" or any(
        entry[field] != plugin[field] for field in ("name", "version")
    ):
        raise ValueError("市场条目与插件清单的路径、名称或版本不一致")
    if not (SKILL / "SKILL.md").is_file():
        raise ValueError(f"技能源缺少 SKILL.md：{SKILL}")

    output = output.absolute()
    output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix="pmo-zcode-", dir=output.parent) as staging:
        candidate = Path(staging) / "marketplace"
        for relative in (MARKETPLACE, MANIFEST):
            destination = candidate / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ADAPTER / relative, destination)
        copy_skill(candidate / PLUGIN / "skills" / ZCODE_SKILL_NAME)

        try:
            output.mkdir()
        except FileExistsError:
            if (output.is_dir() and not output.is_symlink()
                    and not any(path.is_symlink() for path in output.rglob("*"))
                    and files(output) == files(candidate)):
                return output
            raise ValueError(f"输出目录已有其他内容，请指定新目录：{output}") from None
        try:
            candidate.rename(output)
        except OSError:
            output.rmdir()
            raise
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", type=Path, default=ADAPTER / "dist/local-marketplace",
                        help="输出目录，默认 adapters/zcode/dist/local-marketplace")
    args = parser.parse_args()
    try:
        print(build(args.output))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
