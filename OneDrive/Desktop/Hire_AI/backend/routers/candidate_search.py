from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from backend.utils.scoring import score_candidates
from backend.models import Candidate, SessionLocal
import json

router = APIRouter()

class SearchQuery(BaseModel):
    title: str
    skills: List[str]
    location: Optional[str] = None
    type: Optional[str] = None

class CandidateResponse(BaseModel):
    name: str
    email: Optional[str]
    skills: List[str]
    experience: List[dict]
    education: List[dict]
    score: float
    match_percentage: float

@router.post("/search_candidates", response_model=List[CandidateResponse])
async def search_candidates(query: SearchQuery):
    db = SessionLocal()
    try:
        # Fetch candidates from SQLite DB
        candidates_from_db = db.query(Candidate).all()

        # Convert DB objects to dictionaries and parse JSON fields
        candidate_list_for_scoring = []
        for c in candidates_from_db:
            candidate_list_for_scoring.append({
                "name": c.name,
                "email": c.email,
                "skills": json.loads(c.skills) if c.skills else [],
                "experience": json.loads(c.experience) if c.experience else [],
                "education": json.loads(c.education) if c.education else []
            })

        job_requirements = {
            'title': query.title,
            'skills': query.skills,
            'location': query.location,
            'type': query.type
        }
        scored_candidates = score_candidates(candidate_list_for_scoring, job_requirements)
        return scored_candidates
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close() 