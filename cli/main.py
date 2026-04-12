import argparse
import json

from agents.debug_agent import debug_error
from agents.search_agent import search_code
from core.engine import build_context_with_files, build_prompt
from llm.provider import ask_llm


def explain(path: str, model: str, max_files: int, max_chars: int, include_tests: bool) -> tuple[str, list[str]]:
    context, selected_files = build_context_with_files(
        path,
        max_files=max_files,
        max_chars=max_chars,
        include_tests=include_tests,
    )
    prompt = build_prompt(context, "Explain this codebase", selected_files)
    return ask_llm(prompt, model), selected_files


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DevOS AI CLI v3")
    parser.add_argument("command", choices=["explain", "search", "debug"], help="Command to run")
    parser.add_argument("target", help="Repository path for explain/search, file path for debug")
    parser.add_argument("query", nargs="?", default=None, help="Search query")
    parser.add_argument("--model", default="auto", choices=["openrouter", "google", "auto"])
    parser.add_argument("--max-files", type=int, default=8)
    parser.add_argument("--max-chars", type=int, default=1400)
    parser.add_argument("--include-tests", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.command == "explain":
        result, selected_files = explain(
            args.target,
            args.model,
            args.max_files,
            args.max_chars,
            args.include_tests,
        )

        if args.as_json:
            print(json.dumps({"selected_files": selected_files, "result": result}, indent=2))
            return

    elif args.command == "search":
        if not args.query:
            raise SystemExit("search command requires a query")
        result = search_code(args.target, args.query, args.model)
        selected_files = None

    else:
        result = debug_error(args.target, args.model)
        selected_files = None

    print("💡 Result:\n")
    print(result)

    if selected_files:
        print("\n📁 Selected files:")
        for file_path in selected_files:
            print(f"- {file_path}")


if __name__ == "__main__":
    main()
