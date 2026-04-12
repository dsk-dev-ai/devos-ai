import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from core.v3.context_builder import rank_files, score_file


def test_score_file_prioritizes_engine_and_python():
    assert score_file("/tmp/core/engine.py") > score_file("/tmp/docs/readme.md")


def test_rank_files_excludes_tests_by_default():
    files = [
        "repo/core/engine.py",
        "repo/tests/test_engine.py",
        "repo/cli/main.py",
    ]
    ranked = rank_files(files)
    assert "repo/tests/test_engine.py" not in ranked


def test_rank_files_can_include_tests():
    files = [
        "repo/core/engine.py",
        "repo/tests/test_engine.py",
    ]
    ranked = rank_files(files, include_tests=True)
    assert "repo/tests/test_engine.py" in ranked
