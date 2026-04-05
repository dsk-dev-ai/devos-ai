import os

IGNORE_DIRS = {
    ".venv", "__pycache__", ".git", "node_modules",
    "dist", "build",
    "apps",        
    "frontend",    
    "infrastructure"
}

EXTENSIONS = (".py", ".js", ".ts", ".tsx")


def get_code_files(repo_path):
    code_files = []

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if file.endswith(EXTENSIONS):
                code_files.append(os.path.join(root, file))

    return code_files


def read_files(files, max_chars=800):
    contents = []

    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                text = f.read()[:max_chars]
                contents.append(f"\n# FILE: {file}\n{text}")
        except:
            continue

    return "\n\n".join(contents)