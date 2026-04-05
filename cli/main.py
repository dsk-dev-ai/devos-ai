import sys
from core.engine import build_context, build_prompt
from llm.provider import ask_llm
from agents.debug_agent import debug_error
from agents.search_agent import search_code


def explain(path, model):
    context = build_context(path)
    prompt = build_prompt(context, "Explain this codebase")
    return ask_llm(prompt, model)


def main():
    if len(sys.argv) < 3:
        print("""
Usage:
  explain <path> [--model openrouter|google|auto]
  search <path> "<query>" [--model openrouter|google|auto]
  debug <file> [--model openrouter|google|auto]
""")
        return

    command = sys.argv[1]
    model = "auto"

    if "--model" in sys.argv:
        idx = sys.argv.index("--model")
        if idx + 1 < len(sys.argv):
            model = sys.argv[idx + 1]

    print("🔍 Processing...\n")

    if command == "explain":
        result = explain(sys.argv[2], model)

    elif command == "search":
        result = search_code(sys.argv[2], sys.argv[3], model)

    elif command == "debug":
        result = debug_error(sys.argv[2], model)

    else:
        result = "❌ Unknown command"

    print("💡 Result:\n")
    print(result)


if __name__ == "__main__":
    main()
