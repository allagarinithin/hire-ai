from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class JobQuery(BaseModel):
    description: str

class ParsedJob(BaseModel):
    title: str
    skills: List[str]
    location: str
    type: str

@router.post("/parse_query", response_model=ParsedJob)
async def parse_query(query: JobQuery):
    try:
        # TODO: Implement actual parsing logic using OpenAI or similar
        # This is a mock response for now
        return ParsedJob(
            title="Senior Software Engineer",
            skills=["Python", "FastAPI", "React", "TypeScript"],
            location="Remote",
            type="Full-time"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 