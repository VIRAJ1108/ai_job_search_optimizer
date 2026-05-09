from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from backend.database.connection import Base

class Resume(Base):

    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    extracted_skills = Column(Text)

    projects = Column(Text)

    experience = Column(Text)

    education = Column(Text)

    certifications = Column(Text)

class JobDescription(Base):

    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)

    role = Column(String)

    extracted_skills = Column(Text)

    experience_level = Column(String)

    raw_text = Column(Text)

class MatchResult(Base):

    __tablename__ = "match_results"

    id = Column(Integer, primary_key=True, index=True)

    semantic_match_score = Column(Float)

    matching_skills = Column(Text)

    missing_skills = Column(Text)

    strengths = Column(Text)

    weaknesses = Column(Text)

    recommendations = Column(Text)

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id")
    )

    jd_id = Column(
        Integer,
        ForeignKey("job_descriptions.id")
    )

    resume = relationship("Resume")

    job_description = relationship(
        "JobDescription"
    )

class Application(Base):

    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String)

    role = Column(String)

    status = Column(String)

    notes = Column(Text)

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id")
    )

    jd_id = Column(
        Integer,
        ForeignKey("job_descriptions.id")
    )

    match_result_id = Column(
        Integer,
        ForeignKey("match_results.id")
    )