import os
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient("http://qdrant:6333")

def index_repo(path):

    docs = []

    for root, _, files in os.walk(path):

        for f in files:
            if f.endswith((".py",".js",".ts",".rs")):

                with open(os.path.join(root,f)) as file:
                    docs.append(file.read())

    vectors = model.encode(docs)

    for i, doc in enumerate(docs):

        client.upsert(
            collection_name="repo_vectors",
            points=[{
                "id": i,
                "vector": vectors[i],
                "payload": {"text": doc}
            }]
        )