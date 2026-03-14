from sentence_transformers import SentenceTransformer
from config import MODEL

model = SentenceTransformer(MODEL)

def embed(texts):
    return model.encode(texts)