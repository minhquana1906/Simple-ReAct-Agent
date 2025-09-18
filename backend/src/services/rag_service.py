# RAG workflow using LlamaIndex, LangChain, and Qdrant
from backend.src.services.vector_db_service import upsert_vector, search_vector

# Placeholder for embedding and LLM logic
# In production, use LlamaIndex/LangChain to generate embeddings and call OpenAI API


def add_document_embedding(doc_id: int, embedding: list[float], metadata: dict):
    upsert_vector(doc_id, embedding, metadata)


def query_rag(query_embedding: list[float], top_k: int = 3):
    hits = search_vector(query_embedding, top_k=top_k)
    # In production, rerank and generate answer with LLM
    return [hit.payload for hit in hits]
