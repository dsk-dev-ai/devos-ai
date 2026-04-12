from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from core.parser import get_code_files, read_files


KEYWORD_WEIGHTS = {
    "main": 6,
    "app": 6,
    "engine": 7,
    "cli": 5,
    "api": 5,
    "router": 4,
    "agent": 4,
    "provider": 4,
    "pipeline": 3,
    "config": 2,
    "test": 1,
}


@dataclass(frozen=True)
class BuildOptions:
    max_files: int = 8
    max_chars: int = 1400
    include_tests: bool = False


def score_file(path: str) -> int:
    lowered = path.lower()
    score = 0

    for keyword, weight in KEYWORD_WEIGHTS.items():
        if keyword in lowered:
            score += weight

    suffix = Path(lowered).suffix
    if suffix in {".py", ".rs"}:
        score += 2
    elif suffix in {".ts", ".tsx", ".js"}:
        score += 1

    return score


def rank_files(files: list[str], include_tests: bool = False) -> list[str]:
    ranked: list[tuple[int, str]] = []

    for file in files:
        if not include_tests and "test" in file.lower():
            continue
        ranked.append((score_file(file), file))

    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return [file for _, file in ranked]


def build_context(repo_path: str, options: BuildOptions | None = None) -> tuple[str, list[str]]:
    opts = options or BuildOptions()
    files = get_code_files(repo_path)
    ranked_files = rank_files(files, include_tests=opts.include_tests)
    selected = ranked_files[: opts.max_files]
    context = read_files(selected, max_chars=opts.max_chars)
    return context, selected
