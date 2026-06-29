from pydantic import BaseModel, EmailStr, Field
from typing import List


class User_profile(BaseModel):
    """Container for a single user profile"""

    name: str = Field(..., min_length=1)
    email: EmailStr
    education: str = Field(..., min_length=1)
    skills: List[str] = Field(..., min_items=1)
    target_role: str = Field(..., min_length=1)