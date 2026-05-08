from fastapi import APIRouter

from backend.parsers.jd_parser import parse_job_description
from backend.parsers.resume_parser import extract_text_from_pdf

from backend.services.matching_service import match_resume_to_jd


router = APIRouter()


@router.post("/match")
def match_resume_and_jd():

    # Resume path
    resume_path = "resumes/Viraj_Lite_CV.pdf"

    # Parse resume
    resume_data = extract_text_from_pdf(
        resume_path
    )

    # Sample JD
    jd_text = """
    We are looking for an AI/ML Engineer with experience in
    Python, Machine Learning, Deep Learning, PyTorch,
    FastAPI, SQL, Computer Vision and LLM applications.

    Candidates with experience in RAG systems,
    LangChain, vector databases, and Generative AI
    applications will be preferred.
    """

    # Parse JD
    jd_data = parse_job_description(
        jd_text
    )

    # Match
    result = match_resume_to_jd(
        resume_data,
        jd_data
    )

    return {
        "resume_data": resume_data,
        "jd_data": jd_data,
        "match_result": result
    }