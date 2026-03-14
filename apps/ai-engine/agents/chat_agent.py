from rag.pipeline import run_rag
import requests
from config import OLLAMA_URL

def chat_with_repo(query):

    prompt = run_rag(query)

    res = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt
        }
    )

    return res.json()["response"]