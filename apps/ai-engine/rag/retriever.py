from qdrant_client import QdrantClient
from config import QDRANT_URL, COLLECTION

client = QdrantClient(url=QDRANT_URL)

def search(query_vector):

    results = client.search(
        collection_name=COLLECTION,
        query_vector=query_vector,
        limit=5
    )

    return [r.payload["text"] for r in results]