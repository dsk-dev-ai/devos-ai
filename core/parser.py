import os
from pathlib import Path
from typing import Iterable

DEFAULT_IGNORE_DIRS = {
    ".venv", "__pycache__", ".git", "node_modules",
    "dist", "build", "apps", "frontend", "infrastructure", "assets"
}

DEFAULT_EXTENSIONS = (".py", ".js", ".ts", ".tsx", ".rs", ".md")


def _iter_code_files(
    repo_path: str,
    ignore_dirs: set[str],
    extensions: tuple[str, ...],
) -> Iterable[Path]:
    root_path = Path(repo_path).resolve()

    for root, dirs, files in os.walk(root_path):
        dirs[:] = sorted(d for d in dirs if d not in ignore_dirs)

        for filename in sorted(files):
            if filename.endswith(extensions):
                yield Path(root) / filename


def get_code_files(
    repo_path: str,
    ignore_dirs: set[str] | None = None,
    extensions: tuple[str, ...] | None = None,
) -> list[str]:
    ignore = ignore_dirs or DEFAULT_IGNORE_DIRS
    exts = extensions or DEFAULT_EXTENSIONS
    return [str(path) for path in _iter_code_files(repo_path, ignore, exts)]


def read_files(files: list[str], max_chars: int = 1200) -> str:
    contents: list[str] = []

    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as source:
                text = source.read()[:max_chars]
            contents.append(f"\n# FILE: {file}\n{text}")
        except (OSError, UnicodeDecodeError):
            continue

    return "\n\n".join(contents)
