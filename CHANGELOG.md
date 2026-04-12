# DevOS AI Changelog

## v3.0.0 - 2026-04-12

### 🚀 Features
- Added a new `core/v3` module with weighted context ranking and modern prompt templates.
- Added advanced explain controls to the CLI: `--max-files`, `--max-chars`, `--include-tests`, and `--json`.
- Added explain output metadata showing the selected files used as context.

### 🔄 Replacements
- Directly replaced the old simplistic context-building flow with the new v3 engine pipeline.
- Replaced ad-hoc CLI argument handling with `argparse` for more reliable command parsing.

### 🛠 Improvements
- Expanded parser extension support and safer file reading behavior.
- Added release notes under `VERSION/3.0.0/CHANGELOG.md`.

## v2.0.0
- CLI-based AI code analyzer
- Code explanation
- Code search
- Debug assistant
- Multi-LLM support
