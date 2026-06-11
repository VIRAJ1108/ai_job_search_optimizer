from fastapi import APIRouter,UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.connection import get_db
from backend.database.crud import create_resume, create_job_description, create_match_result, get_all_job_descriptions, get_all_match_results, get_all_resumes
from backend.parsers.resume_parser import extract_text_from_pdf
from backend.parsers.jd_parser import parse_job_description
from backend.services.matching_service import match_resume_to_jd
from backend.llm.reasoning_engine import generate_match_analysis
import os

router = APIRouter()

@router.post("/run-workflow")
async def run_workflow(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Full AI workflow pipeline
    """

    if not resume.filename.endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are allowed."
        )
    
    # Validate JD
    if not job_description.strip():

        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    # Resume Path
    resume_path = f"temp_{resume.filename}"

    try:
        with open(resume_path, "wb") as file:

            content = await resume.read()

            file.write(content)
        
        # Parse Resume
        resume_data = extract_text_from_pdf(
            resume_path
        )
        print(resume_data)


        # Save Resume
        saved_resume = create_resume(
            db,
            resume.filename,
            resume_data
        )

        # Parse JD
        jd_data = parse_job_description(
            job_description
        )

        if not job_description.strip():

            raise HTTPException(
                status_code=400,
                detail="Job description cannot be empty."
            )
        
        # Save JD
        saved_jd = create_job_description(
            db,
            jd_data,
            job_description
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
    except Exception as e:

        print("ERROR OCCURRED:")
        print(str(e))

        import traceback
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    finally:

        # Cleanup temp PDF
        if os.path.exists(resume_path):

            os.remove(resume_path)

