from langchain_core.prompts import PromptTemplate
from backend.llm.gemini_client import llm
from langchain_core.output_parsers import PydanticOutputParser
from backend.llm.schemas import ResumeAnalysis

parser = PydanticOutputParser(pydantic_object=ResumeAnalysis)
format_instructions = parser.get_format_instructions()


def generate_match_analysis(
    resume_data: dict,
    jd_data: dict,
    match_result: dict
) -> str:
    """
    Generate AI reasoning analysis
    """

    template = """
You are an AI career assistant helping evaluate
a candidate against a job description.

Analyze the candidate professionally and strategically.

RESUME SKILLS:
{resume_skills}

PROJECTS:
{projects}

JOB DESCRIPTION SKILLS:
{jd_skills}

MATCH RESULT:
Semantic Match Score:
{match_score}

Matching Skills:
{matching_skills}

Missing Skills:
{missing_skills}

Your task:

1. Identify key strengths
2. Identify important weaknesses/gaps
3. Suggest strategic resume improvements
4. Suggest which projects should be emphasized
5. Do NOT hallucinate fake experience
6. Keep recommendations practical and concise

{format_instructions}
"""

    prompt = PromptTemplate(
        input_variables=[
            "resume_skills",
            "projects",
            "jd_skills",
            "match_score",
            "matching_skills",
            "missing_skills"
        ],
        template=template
    )

    final_prompt = prompt.format(
        format_instructions=format_instructions,
        resume_skills=resume_data.get("skills"),
        projects=resume_data.get("projects"),
        jd_skills=jd_data.get("skills"),
        match_score=match_result.get(
            "semantic_match_score"
        ),
        matching_skills=match_result.get(
            "matching_skills"
        ),
        missing_skills=match_result.get(
            "missing_skills"
        )
    )

    response = llm.invoke(final_prompt)

    structured_response = parser.parse(response.content)

    return structured_response