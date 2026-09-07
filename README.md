# 🚀 DevOS AI

DevOS AI is a developer-first assistant for understanding codebases faster using structured context extraction and LLM reasoning.

## ✅ Release Status

**Current release: v3.0.0**

v3 introduces a direct replacement of the legacy context engine with a smarter ranking pipeline, advanced CLI controls, and better output structure for explain workflows.

## 🔥 What’s New in v3

- Advanced context ranking with weighted file scoring.
- Direct replacement of the old prompt builder with a stricter “facts vs inference” response format.
- New `core/v3/` module for maintainable architecture.
- New CLI controls: `--max-files`, `--max-chars`, `--include-tests`, and `--json`.
- Improved explain command output with selected file visibility.

## 📦 Project Structure

```text
devos-ai/
├── cli/
├── core/
│   └── v3/
├── llm/
├── agents/
├── apps/
├── infrastructure/
├── docs/
└── scripts/
```

## ⚙️ Installation

```bash
git clone https://github.com/dsk-dev-ai/devos-ai.git
cd devos-ai
pip install -r requirements.txt
```

## ⚡ Usage

### Explain a repository

```bash
python3 -m cli.main explain . --model auto
python3 -m cli.main explain . --max-files 12 --max-chars 2000
python3 -m cli.main explain . --include-tests --json
```

### Search code

```bash
python3 -m cli.main search . "engine"
```

### Debug an error file

```bash
python3 -m cli.main debug error.log
```

## 🛣️ Roadmap

- ✅ v3: advanced context engine and richer CLI controls.
- 🔜 v3.x: smarter semantic retrieval and local embedding cache.
- 🔜 v4: interactive web dashboard with collaborative review mode.

## 📜 License

MIT License.
