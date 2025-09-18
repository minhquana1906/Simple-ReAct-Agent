import os
from fastapi.testclient import TestClient
from fastapi import FastAPI
import tempfile

# Import the FastAPI app (to be implemented)
try:
    from backend.src.api.upload import router as upload_router
except ImportError:
    upload_router = None

app = FastAPI()
if upload_router:
    app.include_router(upload_router)

client = TestClient(app)


def test_upload_pdf():
    if not upload_router:
        assert False, "Upload router not implemented yet"
    with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
        tmp.write(b"%PDF-1.4 test content")
        tmp.seek(0)
        response = client.post(
            "/upload",
            files={"file": (os.path.basename(tmp.name), tmp, "application/pdf")},
        )
    assert response.status_code == 200
    data = response.json()
    assert "filename" in data
    assert data["filename"].endswith(".pdf")
    assert data["content_type"] == "application/pdf"


def test_upload_csv():
    if not upload_router:
        assert False, "Upload router not implemented yet"
    with tempfile.NamedTemporaryFile(suffix=".csv") as tmp:
        tmp.write(b"col1,col2\n1,2\n")
        tmp.seek(0)
        response = client.post(
            "/upload", files={"file": (os.path.basename(tmp.name), tmp, "text/csv")}
        )
    assert response.status_code == 200
    data = response.json()
    assert "filename" in data
    assert data["filename"].endswith(".csv")
    assert data["content_type"] == "text/csv"


def test_upload_invalid_type():
    if not upload_router:
        assert False, "Upload router not implemented yet"
    with tempfile.NamedTemporaryFile(suffix=".exe") as tmp:
        tmp.write(b"MZ fake exe")
        tmp.seek(0)
        response = client.post(
            "/upload",
            files={
                "file": (os.path.basename(tmp.name), tmp, "application/octet-stream")
            },
        )
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "unsupported file type" in data["detail"].lower()
