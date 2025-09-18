from fastapi import APIRouter, UploadFile, File
from backend.src.services.file_service import save_upload_file

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    result = save_upload_file(file)
    return {"filename": result["filename"], "content_type": result["content_type"]}
