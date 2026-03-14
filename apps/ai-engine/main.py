from fastapi import FastAPI
from agents.chat_agent import chat_with_repo

app = FastAPI(title="DevOS AI")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(query: str):
    response = chat_with_repo(query)
    return {"response": response}