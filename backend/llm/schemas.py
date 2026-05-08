from pydantic import BaseModel
from typing import List


class ResumeAnalysis(BaseModel):

    strengths: List[str]

    weaknesses: List[str]

    recommendations: List[str]

    projects_to_emphasize: List[str]