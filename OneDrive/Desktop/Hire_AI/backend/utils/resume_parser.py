import PyPDF2
import io
from typing import Dict, List, Optional
import re

def extract_text_from_pdf(pdf_content: bytes) -> str:
    """
    Extract text content from a PDF file.
    """
    pdf_file = io.BytesIO(pdf_content)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_name(text: str) -> Optional[str]:
    """
    Extract candidate name from resume text.
    """
    # TODO: Implement more sophisticated name extraction
    # This is a simple implementation
    lines = text.split('\n')
    if lines:
        return lines[0].strip()
    return None

def extract_skills(text: str) -> List[str]:
    """
    Extract skills from resume text.
    """
    # TODO: Implement more sophisticated skill extraction
    # This is a simple implementation
    common_skills = [
        "Python", "JavaScript", "Java", "C++", "React", "Angular", "Vue",
        "Node.js", "Express", "Django", "Flask", "FastAPI", "SQL", "NoSQL",
        "MongoDB", "PostgreSQL", "AWS", "Azure", "Docker", "Kubernetes"
    ]
    
    found_skills = []
    for skill in common_skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    
    return found_skills

def extract_experience(text: str) -> List[Dict]:
    """
    Extract work experience from resume text.
    """
    # TODO: Implement more sophisticated experience extraction
    # This is a simple implementation
    experience = []
    
    # Look for common job title patterns
    job_patterns = [
        r"(?i)(senior|junior|lead)?\s*(software|frontend|backend|full-stack|devops)\s*(engineer|developer|architect)",
        r"(?i)(product|project|technical)\s*(manager|lead)",
    ]
    
    for pattern in job_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            # Extract surrounding context
            start = max(0, match.start() - 100)
            end = min(len(text), match.end() + 100)
            context = text[start:end]
            
            experience.append({
                "title": match.group().strip(),
                "company": "Company Name",  # TODO: Extract company name
                "duration": "Duration"      # TODO: Extract duration
            })
    
    return experience

def parse_resume(pdf_content: bytes) -> Dict:
    """
    Parse resume PDF and extract structured information.
    """
    text = extract_text_from_pdf(pdf_content)
    
    return {
        "name": extract_name(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text)
    } 