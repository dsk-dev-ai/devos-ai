import sys
import requests

query = " ".join(sys.argv[1:])

res = requests.post(
    "http://localhost:8000/chat",
    params={"query": query}
)

print(res.json()["response"])