# HireAI Backend

This is the backend service for HireAI, an AI-powered recruitment assistant. The service is built using FastAPI and provides endpoints for job description parsing, resume parsing, candidate search, and email generation.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:
```
# Supabase Configuration
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_key_here

# OpenAI Configuration (for future use)
OPENAI_API_KEY=your_openai_api_key_here

# Server Configuration
PORT=8000
HOST=0.0.0.0
```

4. Run the server:
```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.

## API Endpoints

1. `/api/parse_query` (POST)
   - Parses a job description into structured data
   - Input: Plain text job description
   - Output: Structured job data (title, skills, location, type)

2. `/api/upload_resume` (POST)
   - Uploads and parses a resume PDF
   - Input: PDF file
   - Output: Structured candidate data (name, skills, experience)

3. `/api/search_candidates` (POST)
   - Searches and ranks candidates based on job requirements
   - Input: Job requirements
   - Output: Ranked list of matching candidates

4. `/api/generate_email` (POST)
   - Generates a personalized outreach email
   - Input: Candidate info and job details
   - Output: Email subject and body

## Development

The project structure is organized as follows:

```
backend/
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── routers/            # API route handlers
│   ├── query_parser.py
│   ├── resume_parser.py
│   ├── candidate_search.py
│   └── email_generator.py
└── utils/              # Utility functions
    ├── supabase_client.py
    ├── scoring.py
    └── resume_parser.py
```

## TODO

- Implement actual parsing logic using OpenAI or similar
- Improve resume parsing accuracy
- Add authentication and authorization
- Add rate limiting
- Add error logging
- Add unit tests
- Add integration tests 