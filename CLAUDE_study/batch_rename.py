#!/usr/bin/env python3
"""
文件批量重命名工具 - Day 7 完整小项目

功能：
- 按前缀批量重命名文件
- 按序号重命名文件
- 预览模式（不实际执行）
"""

import os
import sys
import argparse
import re
from pathlib import Path


def preview_rename(files: list[str], prefix: str, start: int = 1) -> list[tuple[str, str]]:
    """预览重命名结果"""
    results = []
    for i, filepath in enumerate(files):
        original = Path(filepath)
        new_name = f"{prefix}_{start + i:03d}{original.suffix}"
        results.append((filepath, new_name))
    return results


def batch_rename(files: list[str], prefix: str, start: int = 1, dry_run: bool = True):
    """批量重命名文件"""
    preview = preview_rename(files, prefix, start)

    print(f"\n将重命名 {len(preview)} 个文件:")
    print("-" * 60)
    for old, new in preview:
        print(f"  {Path(old).name} -> {new}")

    if dry_run:
        print("\n[预览模式] 如需实际执行，请使用 --execute 参数")
        return

    confirm = input("\n确认执行? (y/n): ")
    if confirm.lower() != "y":
        print("已取消")
        return

    for old_path, new_name in preview:
        old = Path(old_path)
        new = old.parent / new_name
        old.rename(new)
        print(f"✓ 重命名: {old.name} -> {new_name}")

    print(f"\n完成! 共重命名 {len(preview)} 个文件")


def main():
    parser = argparse.ArgumentParser(description="文件批量重命名工具")
    parser.add_argument("directory", help="目标目录")
    parser.add_argument("-p", "--prefix", default="file", help="文件名前缀")
    parser.add_argument("-s", "--start", type=int, default=1, help="起始序号")
    parser.add_argument("-e", "--execute", action="store_true", help="执行重命名（默认预览）")
    parser.add_argument("-i", "--include", default=".*", help="包含的文件类型（正则）")
    parser.add_argument("-x", "--exclude", default="^$", help="排除的文件类型（正则）")

    args = parser.parse_args()

    # 获取目录中的文件
    directory = Path(args.directory)
    if not directory.exists():
        print(f"错误: 目录不存在: {directory}")
        sys.exit(1)

    include_pattern = re.compile(args.include)
    exclude_pattern = re.compile(args.exclude)

    files = []
    for f in directory.iterdir():
        if f.is_file():
            # 检查文件后缀是否匹配 include 模式（需要精确匹配 .xxx 格式）
            suffix_match = include_pattern.search(f.suffix) if f.suffix else False
            # 检查文件名是否匹配 exclude 模式
            exclude_match = exclude_pattern.search(f.name)
            if suffix_match and not exclude_match:
                files.append(str(f))

    # 按文件名排序
    files.sort()

    if not files:
        print("未找到匹配的文件")
        sys.exit(1)

    batch_rename(files, args.prefix, args.start, dry_run=not args.execute)


if __name__ == "__main__":
    main()
