from backend.parsers.jd_parser import parse_job_description


sample_jd = """
We are hiring an AI Engineer with 1-3 years of experience.

Required Skills:
Python, Machine Learning, Deep Learning, PyTorch, FastAPI, SQL

Experience with RAG systems and LLM applications is preferred.
"""


result = parse_job_description(sample_jd)

print(result)