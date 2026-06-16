from pydantic import BaseModel
from typing import List

class AssessmentRequest(BaseModel):
    education: str
    skills: List[str]
    interests: List[str]