from backend.embeddings.similarity import compute_similarity

def normalize_skills(skills: list) -> list:
    """
    Normalize skill names
    """

    normalized = []

    for skill in skills:

        skill = skill.lower().strip()

        normalized.append(skill)

    return normalized

def match_resume_to_jd(
    resume_data: dict,
    jd_data: dict
) -> dict:
    """
    Match resume against JD
    """

    resume_skills = normalize_skills(
    resume_data.get("skills", [])
    )

    jd_skills = normalize_skills(
        jd_data.get("skills", [])
    )

    resume_text = " ".join(resume_skills)

    jd_text = " ".join(jd_skills)

    score = compute_similarity(
        resume_text,
        jd_text
    )

    matching_skills = list(
    set(resume_skills) &
    set(jd_skills)
    )

    missing_skills = list(
    set(jd_skills) -
    set(resume_skills)
    )

    result = {
        "semantic_match_score": score,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills
    }

    return result