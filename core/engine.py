from core.parser import get_code_files, read_files

PRIORITY = ["main", "app", "engine", "cli", "api"]


def rank_files(files):
    scored = []

    for f in files:
        score = 0
        name = f.lower()

        for p in PRIORITY:
            if p in name:
                score += 5

        if "core" in name or "llm" in name:
            score += 3

        scored.append((score, f))

    scored.sort(reverse=True)
    return [f for _, f in scored]


def build_context(repo_path):
    files = get_code_files(repo_path)
    ranked = rank_files(files)

    top_files = ranked[:5]
    return read_files(top_files)


def build_prompt(context, question):
    return f"""
You are a senior software engineer analyzing a real codebase.

STRICT RULES:
- Use ONLY the given code context
- Do NOT assume missing features
- Do NOT mention technologies not present in context

CONTEXT:
{context}

TASK:
{question}

Respond in this format:

1. Purpose
- What this system actually does (based only on code)

2. Architecture
- Real structure (modules, flow)

3. Key Components
- Explain actual files/modules found

4. Execution Flow
- Step-by-step how system works

Keep answer precise, technical, and grounded in code.
"""
