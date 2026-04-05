import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def ask_openrouter(prompt):
    if not OPENROUTER_API_KEY:
        return None

    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=20
        )

        data = res.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        return None

    except:
        return None


def ask_google(prompt):
    if not GOOGLE_API_KEY:
        return None

    try:
        res = requests.post(
            f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GOOGLE_API_KEY}",
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{"parts": [{"text": prompt}]}]
            },
            timeout=30
        )

        data = res.json()

        if "candidates" in data:
            return data["candidates"][0]["content"]["parts"][0]["text"]

        return None

    except:
        return None


def ask_llm(prompt, model="auto"):

    def clean(res):
        if not res:
            return None
        res = str(res).strip()
        return res if len(res) > 10 else None   # IMPORTANT

    # -------- OPENROUTER --------
    if model == "openrouter":
        res = clean(ask_openrouter(prompt))
        return res if res else "❌ OpenRouter returned empty response"

    # -------- GOOGLE --------
    if model == "google":
        res = clean(ask_google(prompt))
        return res if res else "❌ Google returned empty response"

    # -------- AUTO MODE --------
    if model == "auto":
        res = clean(ask_openrouter(prompt))
        if res:
            return res

        res = clean(ask_google(prompt))
        if res:
            return res

        return "❌ All LLM providers failed or returned empty"

    return "❌ Invalid model"
