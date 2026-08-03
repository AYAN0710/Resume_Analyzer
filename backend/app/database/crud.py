from sqlalchemy.orm import Session
from app.database import models
from app.database import schemas

def create_resume(db:Session,resume:schemas.ResumeCreate):
    db_resume=models.Resume(
        filename=resume.filename,
        file_path=resume.file_path,
        extracted_text=resume.extracted_text,
        parsed_sections=resume.parsed_sections
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume

def get_resume(db:Session,resume_id:int):
    return (db.query(models.Resume).filter(models.Resume.id==resume_id).first())

def get_all_resumes(db:Session):
    return (db.query(models.Resume).all())

def delete_resume(db:Session,resume_id:int):
    resume=get_resume(db,resume_id)
    if resume:
        db.delete(resume)
        db.commit()
        return True
    return False

def create_job_description(db:Session,job:schemas.JobDescriptionCreate):
    db_job=models.JobDescription(
        company=job.company,
        role=job.role,
        description=job.description
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_job(db:Session,job_id:int):
    return (db.query(models.JobDescription).filter(models.JobDescription.id==job_id).first())

def create_analysis(db:Session,analysis:schemas.ResumeAnalysisCreate):
    db_analysis=models.ResumeAnalysis(
        resume_id=analysis.resume_id,
        job_id=analysis.job_id,
        ats_score=analysis.ats_score,
        semantic_similarity=analysis.semantic_similarity,
        grammar_score=analysis.grammar_score,
        readibility_score=analysis.readability_score,
        missing_skills=analysis.missing_skills,
        recommendations=analysis.recommendations,
        analytics=analysis.analytics
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis

def get_analysis(db:Session,analysis_id:int):
    return (db.query(models.ResumeAnalysis).filter(models.ResumeAnalysis).filter(models.ResumeAnalysis.id==analysis_id).first())

def add_history(db:Session,analysis_id:int,action:str):
    history=models.AnalysisHistory(analysis_id=analysis_id,action=action)
    db.add(history)
    db.commit()
    db.refresh(history)
    return history

def get_history(db:Session,analysis_id:int):
    return (db.query(models.AnalysisHistory).filter(models.AnalysisHistory.analysis_id==analysis_id).all())