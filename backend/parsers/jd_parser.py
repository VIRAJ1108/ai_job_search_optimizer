import re
COMMON_SKILLS = [
    "python",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "sql",
    "opencv",
    "llm",
    "rag",
    "langchain",
    "fastapi",
    "docker",
    "aws",
    "numpy",
    "pandas",
    "computer vision"
]

def extract_skills_from_jd(jd_text: str) -> list:
    """
    Extract matching skills from JD
    """

    jd_text = jd_text.lower()

    detected_skills = []

    for skill in COMMON_SKILLS:

        if skill in jd_text:
            detected_skills.append(skill)

    return list(set(detected_skills))

def extract_experience_level(jd_text: str) -> str:
    """
    Extract experience requirement
    """

    jd_text = jd_text.lower()

    patterns = [
        r'(\d+)\+?\s+years',
        r'(\d+)\s*-\s*(\d+)\s+years'
    ]

    for pattern in patterns:

        match = re.search(pattern, jd_text)

        if match:
            return match.group()

    return "Not Specified"

def detect_role(jd_text: str) -> str:
    """
    Detect job role
    """

    role_keywords = [
        "machine learning engineer",
        "ai engineer",
        "ml engineer",
        "data scientist",
        "computer vision engineer",
        "genai engineer",
        "python developer"
    ]

    jd_lower = jd_text.lower()

    for role in role_keywords:

        if role in jd_lower:
            return role

    return "Unknown Role"

def parse_job_description(jd_text: str) -> dict:
    """
    Parse job description
    """

    parsed_data = {
        "role": detect_role(jd_text),
        "skills": extract_skills_from_jd(jd_text),
        "experience_level": extract_experience_level(jd_text),
        "raw_text": jd_text
    }

    return parsed_data