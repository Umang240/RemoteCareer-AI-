from pydantic import BaseModel
from typing import List

class SkillGapRequest(BaseModel):
    target_role: str
    current_skills: List[str]