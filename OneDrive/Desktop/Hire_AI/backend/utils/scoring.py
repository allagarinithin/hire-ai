from typing import List, Dict
import numpy as np

def calculate_skill_match(candidate_skills: List[str], required_skills: List[str]) -> float:
    """
    Calculate the skill match score between candidate and required skills.
    """
    if not required_skills:
        return 0.0
    
    # Convert to lowercase for case-insensitive matching
    candidate_skills = [skill.lower() for skill in candidate_skills]
    required_skills = [skill.lower() for skill in required_skills]
    
    # Calculate match score
    matches = sum(1 for skill in required_skills if skill in candidate_skills)
    return matches / len(required_skills)

def calculate_experience_score(experience: List[Dict]) -> float:
    """
    Calculate a score based on the candidate's experience.
    """
    if not experience:
        return 0.0
    
    # Simple scoring based on number of years of experience
    # TODO: Implement more sophisticated experience scoring
    return min(len(experience) * 0.2, 1.0)

def score_candidates(candidates: List[Dict], job_requirements: Dict) -> List[Dict]:
    """
    Score and rank candidates based on job requirements.
    """
    scored_candidates = []
    
    for candidate in candidates:
        # Calculate skill match score
        skill_score = calculate_skill_match(
            candidate['skills'],
            job_requirements['skills']
        )
        
        # Calculate experience score
        experience_score = calculate_experience_score(candidate['experience'])
        
        # Calculate final score (weighted average)
        final_score = (skill_score * 0.7) + (experience_score * 0.3)
        
        # Add score to candidate data
        candidate['score'] = final_score
        candidate['match_percentage'] = round(final_score * 100)
        scored_candidates.append(candidate)
    
    # Sort candidates by score in descending order
    scored_candidates.sort(key=lambda x: x['score'], reverse=True)
    
    return scored_candidates 