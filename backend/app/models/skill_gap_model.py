from pydantic import BaseModel, Field
from typing import List

class SkillGapRequest(BaseModel):
    target_role: str = Field(..., min_length=1)
    current_skills: List[str] = Field(..., min_items=1)