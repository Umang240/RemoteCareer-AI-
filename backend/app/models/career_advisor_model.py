from pydantic import BaseModel, Field
from typing import List


class CareerAdviceRequest(BaseModel):
    education: str = Field(..., min_length=1)
    skills: List[str] = Field(..., min_items=1)
    target_role: str = Field(..., min_length=1)