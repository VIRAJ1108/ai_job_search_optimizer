from fastapi import APIRouter, UploadFile, File

from backend.services.resume_service import process_resume_upload


router = APIRouter()


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    extracted_text = process_resume_upload(file)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text
    }