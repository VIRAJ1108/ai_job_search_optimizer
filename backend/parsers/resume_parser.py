import fitz  # PyMuPDF
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
    "computer vision",
    "generative ai",
    "faiss",
    "huggingface"
]


SECTION_HEADERS = {
    "skills": ["skills", "technical skills", "core competencies"],
    "projects": ["projects", "personal projects"],
    "education": ["education", "academic background"],
    "experience": ["experience", "work experience", "internships"],
    "certifications": ["certifications", "certification"],
    "achievements": ["achievements", "awards"],
}

SKILL_ALIASES = {
    "ml": "machine learning",
    "dl": "deep learning",
    "llms": "llm",
    "large language models": "llm",
    "genai": "generative ai",
    "computer vision": "computer vision",
    "cnn": "cnn",
    "cnns": "cnn",
    "rag systems": "rag",
    "retrieval augmented generation": "rag",
}

def clean_resume_text(text: str) -> str:
    """
    Cleans extracted resume text
    """

    # Remove invisible unicode characters
    text = re.sub(r'[\u200b\u200c\u200d\uFEFF]', '', text)

    # Replace multiple spaces/tabs with single space
    text = re.sub(r'[ \t]+', ' ', text)

    # Replace excessive newlines
    text = re.sub(r'\n+', '\n', text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text


def extract_sections(text: str) -> dict:
    """
    Extract resume sections dynamically
    """

    sections = {}

    current_section = "other"

    sections[current_section] = []

    lines = text.split("\n")

    for line in lines:

        clean_line = line.strip().lower()

        found_section = None

        for section, keywords in SECTION_HEADERS.items():

            if clean_line in keywords:
                found_section = section
                break

        if found_section:

            current_section = found_section

            if current_section not in sections:
                sections[current_section] = []

        else:
            sections[current_section].append(line)

    # Convert list to string
    for section in sections:
        sections[section] = "\n".join(
            sections[section]
        ).strip()

    return sections


def extract_skills(skills_text: str) -> list:
    """
    Extract canonical skills from skills section
    """

    if not skills_text:
        return []

    skills_text = skills_text.lower()

    detected_skills = set()

    # Detect direct common skills
    for skill in COMMON_SKILLS:

        if skill in skills_text:
            detected_skills.add(skill)

    # Detect aliases
    for alias, canonical in SKILL_ALIASES.items():

        if alias in skills_text:
            detected_skills.add(canonical)

    return list(detected_skills)

def infer_skills_from_projects(projects_text: str) -> list:
    """
    Infer skills from project descriptions
    """

    if not projects_text:
        return []

    projects_text = projects_text.lower()

    inferred_skills = set()

    # Detect common skills
    for skill in COMMON_SKILLS:

        if skill in projects_text:
            inferred_skills.add(skill)

    # Detect aliases
    for alias, canonical in SKILL_ALIASES.items():

        if alias in projects_text:
            inferred_skills.add(canonical)

    return list(inferred_skills)


def extract_projects(projects_text: str) -> list:
    """
    Extract structured project information
    """

    if not projects_text:
        return []

    lines = projects_text.split("\n")

    projects = []

    current_project = None

    for line in lines:

        line = line.strip()

        # Detect new project title
        if line.startswith("●"):

            # Save previous project
            if current_project:
                projects.append(current_project)

            current_project = {
                "title": line.replace(
                    "●",
                    ""
                ).strip(),

                "description": ""
            }

        else:

            if current_project and line:

                current_project[
                    "description"
                ] += line + " "

    # Append last project
    if current_project:
        projects.append(current_project)

    return projects


def structure_resume_data(sections: dict) -> dict:
    """
    Convert parsed sections into structured resume data
    """

    explicit_skills = extract_skills(
        sections.get("skills", "")
    )

    project_skills = infer_skills_from_projects(
        sections.get("projects", "")
    )

    combined_skills = list(set(
        explicit_skills + project_skills
    ))

    structured_data = {
        "education": sections.get("education", ""),
        "experience": sections.get("experience", ""),
        "skills": combined_skills,
        "projects": extract_projects(
            sections.get("projects", "")
        ),
        "certifications": sections.get(
            "certifications", ""
        ),
        "achievements": sections.get(
            "achievements", ""
        )
    }

    return structured_data


def extract_text_from_pdf(pdf_path: str) -> dict:
    """
    Extract and structure resume data from PDF
    """

    document = fitz.open(pdf_path)

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()

    cleaned_text = clean_resume_text(
        extracted_text
    )

    parsed_sections = extract_sections(
        cleaned_text
    )

    structured_resume = structure_resume_data(
        parsed_sections
    )

    return structured_resume