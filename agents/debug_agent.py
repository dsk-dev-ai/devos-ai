from llm.provider import ask_llm


def debug_error(file_path, model):
    try:
        with open(file_path, "r") as f:
            error = f.read().strip()
    except FileNotFoundError:
        return f"❌ File not found: {file_path}"

    if not error:
        return "❌ Error file is empty"

    prompt = f"""
You are a senior software engineer.

Debug this error:

{error}

Explain clearly:

1. Root cause
2. Why it happens
3. Step-by-step fix
4. Example fix
"""

    result = ask_llm(prompt, model)

    if not result:
        return "❌ No response from LLM"

    return result