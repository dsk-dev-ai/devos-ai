# 🚀 DevOS AI

CLI-based AI tool for analyzing and explaining codebases using structured context extraction and LLM reasoning.

---

## ✨ Introduction

DevOS AI is a developer-first tool designed to help engineers quickly understand unfamiliar codebases.

Instead of manually reading hundreds of files, DevOS intelligently extracts relevant parts of a repository, builds structured context, and uses Large Language Models (LLMs) to generate clear, high-level explanations of architecture and functionality.

---

## 📚 Table of Contents

- Overview
- Features
- How It Works
- Architecture
- Project Structure
- Installation
- Usage
- Example Output
- Demo
- Roadmap
- Configuration
- Dependencies
- Contributing
- Troubleshooting
- License
- Author

---

## 🔍 Overview

DevOS AI transforms codebases into understandable insights by combining:

- Smart file selection
- Context-aware prompt generation
- LLM-powered reasoning

👉 It acts like a **codebase explainer engine**, helping developers onboard faster and debug smarter.

---

## 🔥 Features

- 🔍 Analyze any codebase using AI  
- 🧠 Structured context extraction  
- 🏗 Architecture-level explanations  
- ⚙️ Modular design (CLI + Core + LLM)  
- 🌐 Multi-LLM support (OpenRouter + Google)  
- 💻 CLI-first developer experience  

---

## 🧠 How It Works

### Pipeline


CLI → Context Builder → Prompt Engine → LLM → Output


### Step-by-Step

1. Extract important files from the repository  
2. Rank and filter relevant code  
3. Build structured context  
4. Generate optimized prompts  
5. Send to LLM for reasoning  
6. Output structured explanation  

---

## 🏗 Architecture

| Module | Description |
|--------|------------|
| `cli/` | Command-line interface |
| `core/` | Context building + prompt generation |
| `llm/` | LLM provider integration |

---

## 📂 Project Structure


devos-ai/
├── cli/
├── core/
├── llm/
├── agents/
├── apps/
├── frontend/
├── infrastructure/
├── docs/
├── scripts/


---

## ⚙️ Installation

### Prerequisites

- Python 3.9+
- API key (OpenRouter or Google Gemini)

### Setup

git clone https://github.com/dsk-dev-ai/devos-ai.git
cd devos-ai
pip install -r requirements.txt

## ⚡ Usage

🔍 Explain Codebase
python3 -m cli.main explain .

🔎 Search Code
python3 -m cli.main search . "engine"

🐞 Debug Error
python3 -m cli.main debug error.log

🧠 Choose Model
python3 -m cli.main explain . --model openrouter
python3 -m cli.main explain . --model google
python3 -m cli.main explain . --model auto

## 🧠 Example Output

1. Purpose
CLI-based AI tool for analyzing codebases...

2. Architecture Overview
CLI → Core → LLM → Output

3. Key Components
- CLI
- Core Engine
- LLM Provider

### Example:
At (assets/images/) & (assets/videos/)

## 🚀 Roadmap

✅ V2 (Current)
CLI-based code analyzer
Context ranking system
Multi-LLM support
Search + Debug commands

🔜 V3 (Upcoming)
🔍 Advanced file-level search
🐞 Smart stack trace debugging
⚡ RAG (vector search)
📦 Global CLI install (devos)
🌐 Web dashboard

## ⚙️ Configuration

Create .env file:

OPENROUTER_API_KEY=your_key
GOOGLE_API_KEY=your_key

## 📦 Dependencies

Python standard library
requests
python-dotenv

## 🤝 Contributing

Contributions are welcome!

You can help with:

Improving context extraction
Enhancing LLM prompts
Adding new CLI features
UI/UX improvements

## 🛠 Troubleshooting

1. LLM not working
Check API keys in .env
Verify internet connection
2. No output
Ensure valid project path
Check file permissions
3. Timeout / Slow response
Reduce context size
Check API limits

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Darshan Kachare
AI Developer • Open Source Contributor

GitHub: https://github.com/dsk-dev-ai

## ⭐ Support

If you find this useful:

⭐ Star the repository
🐛 Report issues
🤝 Contribute
🚀 Project Status
🔥 Production-ready CLI
🔥 Recruiter-friendly
🔥 Scalable foundation

---
