from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List, Optional
import PyPDF2
import io
from backend.utils.resume_parser import parse_resume
from backend.models import Candidate, SessionLocal
import json

router = APIRouter()

class CandidateInfo(BaseModel):
    name: str
    email: Optional[str]
    skills: List[str]
    experience: List[dict]
    education: List[dict]

@router.post("/upload_resume", response_model=CandidateInfo)
async def upload_resume(file: UploadFile = File(...)):
    db = SessionLocal()
    try:
        if not file.filename.endswith('.pdf'):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed")

        contents = await file.read()
        candidate_info = parse_resume(contents)

        # Save to SQLite DB
        candidate_obj = Candidate(
            name=candidate_info['name'],
            email=candidate_info.get('email'),
            skills=json.dumps(candidate_info['skills']),
            experience=json.dumps(candidate_info['experience']),
            education=json.dumps(candidate_info.get('education', []))
        )
        db.add(candidate_obj)
        db.commit()
        db.refresh(candidate_obj)

        return CandidateInfo(
            name=candidate_obj.name,
            email=candidate_obj.email,
            skills=json.loads(candidate_obj.skills),
            experience=json.loads(candidate_obj.experience),
            education=json.loads(candidate_obj.education)
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close() 