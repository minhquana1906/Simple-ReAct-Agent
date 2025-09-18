from backend.src.services import file_service
import types


class DummyUploadFile:
    def __init__(self, filename, content_type, content):
        self.filename = filename
        self.content_type = content_type
        self.file = types.SimpleNamespace(read=lambda: content)


def test_save_upload_file_pdf():
    file = DummyUploadFile("test.pdf", "application/pdf", b"%PDF-1.4 test")
    result = file_service.save_upload_file(file)
    assert result["filename"].endswith(".pdf")
    assert result["content_type"] == "application/pdf"


def test_save_upload_file_invalid():
    file = DummyUploadFile("test.exe", "application/octet-stream", b"fake")
    try:
        file_service.save_upload_file(file)
    except Exception as e:
        assert "unsupported file type" in str(e).lower()
