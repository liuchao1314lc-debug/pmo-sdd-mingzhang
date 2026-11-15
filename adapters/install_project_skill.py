#!/usr/bin/env python3
"""Install the PMO skill in a project's host-specific discovery directory."""

import argparse
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


SOURCE = Path(__file__).resolve().parents[1] / "package" / "skills" / "pmo"
HOST_DIRECTORIES = {"codex": ".agents", "claude-code": ".claude"}


def files(root):
    return {
        path.relative_to(root): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    }


def existing_instance(target, expected):
    if (target.is_dir() and not target.is_symlink()
            and not any(path.is_symlink() for path in target.rglob("*"))
            and files(target) == expected):
        return target, "已核对现有实例"
    raise ValueError(f"安装位置已被占用，请先确认现有实例的迁移方式：{target}")


def install(project, host):
    project = project.resolve(strict=True)
    if not project.is_dir():
        raise ValueError(f"项目根目录无效：{project}")

    expected = files(SOURCE)
    if Path("SKILL.md") not in expected:
        raise ValueError(f"技能源缺少 SKILL.md：{SOURCE}")

    parent = project
    for name in (HOST_DIRECTORIES[host], "skills"):
        parent = parent / name
        if parent.is_symlink():
            raise ValueError(f"安装路径包含符号链接：{parent}")
        parent.mkdir(exist_ok=True)

    target = parent / "pmo"
    if target.exists() or target.is_symlink():
        return existing_instance(target, expected)

    with TemporaryDirectory(prefix="pmo-", dir=parent.parent) as staging:
        candidate = Path(staging) / "pmo"
        shutil.copytree(SOURCE, candidate, ignore=shutil.ignore_patterns(".DS_Store"))
        if files(candidate) != expected:
            raise ValueError("部署副本与源文件不一致")
        try:
            target.mkdir()
        except FileExistsError:
            return existing_instance(target, expected)
        try:
            candidate.rename(target)
        except OSError:
            target.rmdir()
            raise

    return target, "已安装并核对实例"


def main(default_host=None):
    description = __doc__ if default_host is None else f"Install the PMO skill for {default_host}."
    parser = argparse.ArgumentParser(description=description)
    if default_host is None:
        parser.add_argument("host", choices=HOST_DIRECTORIES, help="目标宿主")
    parser.add_argument("project", type=Path, help="目标项目根目录")
    args = parser.parse_args()
    try:
        target, result = install(args.project, default_host or args.host)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"{exc}\n")
    print(f"{result}：{target}")


if __name__ == "__main__":
    main()
