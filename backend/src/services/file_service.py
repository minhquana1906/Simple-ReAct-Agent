import os
from fastapi import UploadFile, HTTPException

ALLOWED_TYPES = {"application/pdf": ".pdf", "text/csv": ".csv"}

UPLOAD_DIR = os.environ.get("UPLOAD_DIR", "/tmp/react_agent_uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_upload_file(upload_file: UploadFile) -> dict:
    if upload_file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400, detail="Unsupported file type. Only PDF and CSV allowed."
        )
    ext = ALLOWED_TYPES[upload_file.content_type]
    filename = upload_file.filename
    if not filename.endswith(ext):
        filename += ext
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as f:
        f.write(upload_file.file.read())
    return {
        "filename": filename,
        "content_type": upload_file.content_type,
        "path": file_path,
    }
