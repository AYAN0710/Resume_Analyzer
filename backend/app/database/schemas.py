from pydantic import BaseModel
from datetime import datetime
from typing import List
from typing import Dict
from typing import Optional

class ResumeCreate(BaseModel):
    filename:str
    file_path:str
    extracted_text:str
    parsed_sections:Dict

class ResumeResponse(BaseModel):
    id:int
    filename:str
    file_path:str
    extracted_text:str
    parsed_sections:Dict
    uploaded_at:datetime
    class Config:
        from_attributes=True
        
class JobDescriptionCreate(BaseModel):
    company:str
    role:str
    description:str
    
class JobDescriptionResponse(BaseModel):
    id:int
    company:str
    role:str
    description:str
    uploaded_at:datetime
    class Config:
        from_attributes=True #read data directly from class or db objects instad of expecting a dictionary
      
class ResumeAnalysisCreate(BaseModel):
    resume_id:int
    job_id:int
    ats_score:float
    semantic_similarity:float
    grammar_score:float
    readability_score:float
    missing_skills:List[str]
    recommendations:List[str]
    analytics:Dict 
    
class ResumeAnalysisResponse(BaseModel):
    id:int
    resume_id:int
    job_id:int
    ats_score:float
    semantic_similarity:float
    grammar_score:float
    readability_score:float
    missing_skills:List[str]
    recommendations:List[str]
    analytics:Dict 
    created_at:datetime
    class Config:
        from_attributes=True
        
class HistoryResponse(BaseModel):
    id:int
    analysis_id:int
    action:str
    timestamp:datetime
    class Config:
        from_attributes=True
         
        