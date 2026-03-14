# 🚀 DevOS AI

### The Open-Source AI Operating System for Developers

![GitHub stars](https://img.shields.io/github/stars/dsk-dev-ai/devos-ai?style=social)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Rust](https://img.shields.io/badge/Rust-API-orange)

DevOS AI is an **AI-powered developer platform** that understands repositories, explains code, reviews pull requests, and automates developer workflows.

Think of it as an **AI operating system for software development**.

---

# ✨ Features

* 🔎 **Chat with any repository**
* 🤖 **AI code review for pull requests**
* 🐞 **Debug stack traces instantly**
* 🧪 **Generate unit tests automatically**
* 🧠 **Local LLM support** (Ollama, Mistral, DeepSeek)
* 🖥 **CLI + Web dashboard**
* ⚡ **Fast vector search using Qdrant**
* 🐳 **Docker-based infrastructure**

---

# 🧠 How DevOS AI Works

DevOS AI uses a **RAG (Retrieval Augmented Generation)** pipeline.

Repository → Code chunks → Embeddings → Vector database → AI reasoning → Answer

---

# 🏗 Architecture

![DevOS Architecture](docs/architecture-diagram.png)

Core components:

* Rust API Gateway
* Python AI Engine
* Worker services
* Qdrant vector database
* Ollama LLM runtime
* Next.js frontend

---

# ⚡ Quick Start

## 1️⃣ Start Infrastructure

```bash
docker compose -f infrastructure/docker-compose.yml up
```

---

## 2️⃣ Index a Repository

```bash
python scripts/index_repo.py ./myrepo
```

---

## 3️⃣ Ask DevOS AI

```bash
python cli/devos.py "Explain authentication logic"
```

---

# 📂 Project Structure

```
devos-ai
│
├ apps
│ ├ ai-engine
│ ├ api-gateway
│ └ worker
│
├ frontend
├ cli
├ scripts
├ infrastructure
├ docs
├ examples
```

---

# 🧪 Example Usage

```bash
python cli/devos.py "Explain the authentication system"
```

Example response:

```
The authentication module checks user credentials and validates
the request using token-based verification...
```

---

# 🗺 Roadmap

### Phase 1

* Repository indexing
* Chat with codebase
* Vector search

### Phase 2

* AI PR review
* Debug assistant
* Test generation

### Phase 3

* Autonomous developer agents
* Plugin ecosystem
* Team collaboration tools

---

# 🤝 Contributing

Contributions are welcome!

Please read:

* CONTRIBUTING.md
* CODE_OF_CONDUCT.md

You can help with:

* new AI agents
* performance improvements
* UI improvements
* documentation

---

# ⭐ Support the Project

If DevOS AI helps you:

⭐ Star the repository
🐛 Open issues
🤝 Contribute code

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Darshan Kachare**

AI Developer • Open Source Contributor

GitHub: https://github.com/dsk-dev-ai
