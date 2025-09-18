from fastapi.testclient import TestClient
from fastapi import FastAPI

try:
    from backend.src.api.query import router as query_router
except ImportError:
    query_router = None

app = FastAPI()
if query_router:
    app.include_router(query_router)

client = TestClient(app)


def test_query_rag():
    if not query_router:
        assert False, "Query router not implemented yet"
    # Simulate a RAG query
    response = client.post("/query", json={"query": "What is in the document?"})
    assert response.status_code in (200, 501)  # 501 if not implemented
    data = response.json()
    assert "result" in data or "detail" in data
