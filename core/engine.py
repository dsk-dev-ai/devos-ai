from __future__ import annotations

from core.v3 import BuildOptions
from core.v3 import build_context as build_context_v3
from core.v3 import build_prompt as build_prompt_v3


def build_context(
    repo_path: str,
    max_files: int = 8,
    max_chars: int = 1400,
    include_tests: bool = False,
) -> str:
    options = BuildOptions(
        max_files=max_files,
        max_chars=max_chars,
        include_tests=include_tests,
    )
    context, _ = build_context_v3(repo_path, options)
    return context


def build_context_with_files(
    repo_path: str,
    max_files: int = 8,
    max_chars: int = 1400,
    include_tests: bool = False,
) -> tuple[str, list[str]]:
    options = BuildOptions(
        max_files=max_files,
        max_chars=max_chars,
        include_tests=include_tests,
    )
    return build_context_v3(repo_path, options)


def build_prompt(context: str, question: str, selected_files: list[str] | None = None) -> str:
    return build_prompt_v3(context, question, selected_files)
