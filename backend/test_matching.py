# from backend.parsers.jd_parser import parse_job_description
# from backend.services.matching_service import match_resume_to_jd


# resume_data = {
#     "skills": [
#         "Python",
#         "Machine Learning",
#         "Deep Learning",
#         "PyTorch",
#         "FastAPI",
#         "SQL"
#     ]
# }


# sample_jd = """
# We are hiring an AI Engineer with experience in:
# Python, Machine Learning, TensorFlow, Docker,
# FastAPI, SQL and LLM applications.
# """


# jd_data = parse_job_description(sample_jd)

# result = match_resume_to_jd(
#     resume_data,
#     jd_data
# )

# print(result)


from backend.parsers.resume_parser import extract_text_from_pdf
from backend.parsers.jd_parser import parse_job_description

from backend.services.matching_service import match_resume_to_jd


# Path to your actual resume PDF
resume_path = "resumes/Viraj_Lite_CV.pdf"


# Parse Resume
resume_data = extract_text_from_pdf(resume_path)


# Real Job Description
sample_jd = """
We are looking for an AI/ML Engineer with experience in
Python, Machine Learning, Deep Learning, PyTorch,
FastAPI, SQL, Computer Vision and LLM applications.

Candidates with experience in RAG systems,
LangChain, vector databases, and Generative AI
applications will be preferred.

0-2 years experience preferred.
"""


# Parse JD
jd_data = parse_job_description(sample_jd)


# Match Resume vs JD
result = match_resume_to_jd(
    resume_data,
    jd_data
)


print("\n========= RESUME DATA =========")
print(resume_data)

print("\n========= JD DATA =========")
print(jd_data)

print("\n========= MATCH RESULT =========")
print(result)