from core.parser import get_code_files
from llm.provider import ask_llm


def search_code(repo_path, query, model):
    files = get_code_files(repo_path)

    matches = []

    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()

                for i, line in enumerate(lines):
                    if query.lower() in line.lower():
                        snippet = "".join(lines[max(0, i-2):i+3])

                        matches.append(f"""
FILE: {file}
LINE: {i+1}
CODE:
{snippet}
""")

                        if len(matches) >= 5:
                            break

        except:
            continue

    if not matches:
        return "❌ No matches found"

    context = "\n\n".join(matches)

    prompt = f"""
You are a senior software engineer analyzing search results from a codebase.

User query: "{query}"

Code snippets:
{context}

IMPORTANT:
- Do NOT describe prompts or text
- Focus on actual code logic
- Ignore placeholder strings

Give a professional answer:

1. Relevant functionality found
- What real functionality matches the query

2. Where it exists
- File names and modules

3. How it works
- Explain logic of code (not text)

4. Summary
- What developer should understand from this

Be precise, technical, and useful.
"""

    result = ask_llm(prompt, model)

    if not result or "❌" in result:
        return "❌ No meaningful response from LLM for search"

    return result