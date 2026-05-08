from backend.parsers.resume_parser import extract_text_from_pdf
from backend.parsers.jd_parser import parse_job_description

from backend.services.matching_service import match_resume_to_jd

from backend.llm.reasoning_engine import (
    generate_match_analysis
)


# Resume Path
resume_path = "resumes/Viraj_Lite_CV.pdf"


# Parse Resume
resume_data = extract_text_from_pdf(
    resume_path
)


# Sample Job Description
sample_jd = """
We are looking for an AI/ML Engineer with experience in
Python, Machine Learning, Deep Learning, PyTorch,
FastAPI, SQL, Computer Vision and LLM applications.

Candidates with experience in RAG systems,
LangChain, vector databases, and Generative AI
applications will be preferred.

0-2 years of experience preferred.
"""


# Parse JD
jd_data = parse_job_description(
    sample_jd
)


# Match Resume vs JD
match_result = match_resume_to_jd(
    resume_data,
    jd_data
)


# Generate AI Analysis
analysis = generate_match_analysis(
    resume_data,
    jd_data,
    match_result
)


print("\n========= RESUME DATA =========\n")
print(resume_data)

print("\n========= JD DATA =========\n")
print(jd_data)

print("\n========= MATCH RESULT =========\n")
print(match_result)

print("\n========= AI ANALYSIS =========\n")
print(analysis)