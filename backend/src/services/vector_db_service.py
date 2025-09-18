from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, Distance, VectorParams
import os

QDRANT_HOST = os.environ.get("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.environ.get("QDRANT_PORT", 6333))
COLLECTION_NAME = "react_agent_docs"

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)


def ensure_collection():
    if COLLECTION_NAME not in [c.name for c in client.get_collections().collections]:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE),
        )


def upsert_vector(id: int, vector: list[float], payload: dict):
    ensure_collection()
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[PointStruct(id=id, vector=vector, payload=payload)],
    )


def search_vector(query_vector: list[float], top_k: int = 3):
    ensure_collection()
    hits = client.search(
        collection_name=COLLECTION_NAME, query_vector=query_vector, limit=top_k
    )
    return hits
