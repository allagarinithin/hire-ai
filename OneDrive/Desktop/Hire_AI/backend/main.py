from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from backend.routers import query_parser, resume_parser, candidate_search, email_generator


load_dotenv()

app = FastAPI(
    title="HireAI API",
    description="Backend API for HireAI - AI-powered recruitment assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from backend.routers import query_parser, resume_parser, candidate_search, email_generator

app.include_router(query_parser.router, prefix="/api", tags=["Query Parser"])
app.include_router(resume_parser.router, prefix="/api", tags=["Resume Parser"])
app.include_router(candidate_search.router, prefix="/api", tags=["Candidate Search"])
app.include_router(email_generator.router, prefix="/api", tags=["Email Generator"])

# 5. Root route
@app.get("/")
async def root():
    return {"message": "Welcome to HireAI API"}
