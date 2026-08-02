from sqlalchemy import Column,Integer,String,Float,DateTime,ForeignKey,Text,JSON
from sqlalchemy.orm import relationship
from datetime import datetime,timezone
from app.database.base import Base

class Resume(Base):
    __tablename__="resumes"
    id=Column(Integer,primary_key=True,index=True)
    filename=Column(String,nullable=False)
    file_path=Column(String,nullable=False)
    extracted_text=Column(Text)
    parsed_sections=Column(JSON)
    uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    analyses=relationship("ResumeAnalysis",back_populates="resume",cascade="all, delete")
    
class JobDescription(Base):
    __tablename__="job_descriptions"
    id=Column(Integer,primary_key=True)
    company=Column(String)
    role=Column(String)
    description=Column(Text)
    uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    analyses=relationship("ResumeAnalysis",back_populates="job")
    
class ResumeAnalysis(Base):
    __tablename__="resume_analysis"
    id=Column(Integer,primary_key=True)
    resume_id=Column(Integer,ForeignKey("resumes.id"))
    job_id=Column(Integer,ForeignKey("job_descriptions.id"))
    ats_score=Column(Float)
    semantic_similarity=Column(Float)
    grammar_score=Column(Float)
    readibility_score=Column(Float)
    missing_skills=Column(JSON)
    recommendations=Column(JSON)
    analytics=Column(JSON)
    created_at=Column(DateTime, default=lambda: datetime.now(timezone.utc))
    resume=relationship("Resume",back_populates="analyses")
    job=relationship("JobDescription",back_populates="analyses")
    history=relationship("AnalysisHistory",back_populates="analysis",cascade="all, delete")
    
class AnalysisHistory(Base):
    __tablename__="analysis_history"
    id=Column(Integer,primary_key=True)
    analysis_id=Column(Integer,ForeignKey("resume_analysis.id"))
    action=Column(String)
    timestamp=Column(DateTime, default=lambda: datetime.now(timezone.utc))
    analysis=relationship("ResumeAnalysis",back_populates="history")
    