import os

from backend.parsers.resume_parser import extract_text_from_pdf


UPLOAD_FOLDER = "resumes"


def process_resume_upload(file) -> str:

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    extracted_text = extract_text_from_pdf(file_path)

    return extracted_text