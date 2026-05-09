from sqlalchemy.orm import Session
from backend.database.models import Resume, JobDescription, MatchResult

def create_resume(
    db: Session,
    filename: str,
    resume_data: dict
):
    """
    Save parsed resume
    """

    resume = Resume(
        filename=filename,
        extracted_skills=str(
            resume_data.get("skills")
        ),
        projects=str(
            resume_data.get("projects")
        ),
        experience=resume_data.get(
            "experience"
        ),
        education=resume_data.get(
            "education"
        ),
        certifications=resume_data.get(
            "certifications"
        )
    )

    db.add(resume)

    db.commit()

    db.refresh(resume)

    return resume
# ----------------------------------------------------

def create_job_description(
    db: Session,
    jd_data: dict,
    raw_text: str
):
    """
    Save parsed job description
    """

    job_description = JobDescription(
        extracted_skills=str(
            jd_data.get("skills")
        ),

        experience_level=jd_data.get(
            "experience_level"
        ),

        raw_text=raw_text
    )

    db.add(job_description)

    db.commit()

    db.refresh(job_description)

    return job_description
# ------------------------------------------------
def create_match_result(
    db: Session,
    match_result: dict,
    analysis,
    resume_id: int,
    jd_id: int
):
    """
    Save match analysis
    """

    result = MatchResult(
        semantic_match_score=match_result.get(
            "semantic_match_score"
        ),

        matching_skills=str(
            match_result.get(
                "matching_skills"
            )
        ),

        missing_skills=str(
            match_result.get(
                "missing_skills"
            )
        ),

        strengths=str(
            analysis.strengths
        ),

        weaknesses=str(
            analysis.weaknesses
        ),

        recommendations=str(
            analysis.recommendations
        ),

        resume_id=resume_id,

        jd_id=jd_id
    )

    db.add(result)

    db.commit()

    db.refresh(result)

    return result