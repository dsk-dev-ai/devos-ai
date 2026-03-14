import os

QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")
COLLECTION = "repo_vectors"
MODEL = "sentence-transformers/all-MiniLM-L6-v2"
OLLAMA_URL = "http://ollama:11434/api/generate"