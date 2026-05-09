from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.database.connection import get_db
from backend.database.crud import create_resume, create_job_description, create_match_result
from backend.parsers.resume_parser import extract_text_from_pdf
from backend.parsers.jd_parser import parse_job_description
from backend.services.matching_service import match_resume_to_jd
from backend.llm.reasoning_engine import generate_match_analysis

router = APIRouter()

@router.post("/run-workflow")
def run_workflow(
    db: Session = Depends(get_db)
):
    """
    Full AI workflow pipeline
    """

    # Resume Path
    resume_path = "resumes/Viraj_Lite_CV.pdf"

    # Parse Resume
    resume_data = extract_text_from_pdf(
        resume_path
    )

    # Save Resume
    saved_resume = create_resume(
        db,
        "Viraj_Lite_CV.pdf",
        resume_data
    )

    # Sample JD
    sample_jd = """
    We are looking for an AI/ML Engineer with experience in
    Python, Machine Learning, Deep Learning, PyTorch,
    FastAPI, SQL, Computer Vision and LLM applications.

    Candidates with experience in RAG systems,
    LangChain, vector databases, and Generative AI
    applications will be preferred.
    """

    # Parse JD
    jd_data = parse_job_description(
        sample_jd
    )

    # Save JD
    saved_jd = create_job_description(
        db,
        jd_data,
        sample_jd
    )

    # Match
    match_result = match_resume_to_jd(
        resume_data,
        jd_data
    )

    # AI Analysis
    analysis = generate_match_analysis(
        resume_data,
        jd_data,
        match_result
    )

    # Save Match Result
    saved_result = create_match_result(
        db,
        match_result,
        analysis,
        saved_resume.id,
        saved_jd.id
    )

    return {
        "message": "Workflow completed successfully!",

        "resume_id": saved_resume.id,

        "job_description_id": saved_jd.id,

        "match_result_id": saved_result.id,

        "semantic_match_score":
            saved_result.semantic_match_score,

        "analysis": {
            "strengths": analysis.strengths,
            "weaknesses": analysis.weaknesses,
            "recommendations":
                analysis.recommendations
        }
    }