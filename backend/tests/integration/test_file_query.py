import io
from fastapi.testclient import TestClient
from fastapi import FastAPI

try:
    from backend.src.api.upload import router as upload_router
    from backend.src.api.query import router as query_router
except ImportError:
    upload_router = None
    query_router = None

app = FastAPI()
if upload_router:
    app.include_router(upload_router)
if query_router:
    app.include_router(query_router)

client = TestClient(app)


def test_file_upload_and_query():
    if not upload_router or not query_router:
        assert False, "Routers not implemented yet"
    # Upload a PDF (simulate)
    pdf_content = b"%PDF-1.4 test content"
    upload_resp = client.post(
        "/upload",
        files={"file": ("test.pdf", io.BytesIO(pdf_content), "application/pdf")},
    )
    assert upload_resp.status_code == 200
    # Query the document (simulate)
    query_resp = client.post("/query", json={"query": "What is in the document?"})
    assert query_resp.status_code in (200, 501)
    data = query_resp.json()
    assert "result" in data or "detail" in data
