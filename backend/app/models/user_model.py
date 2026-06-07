from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional


class User_profile(BaseModel):
    """Container for a single user profile"""

    name: str = Field(...)
    education: str = Field(...)
    skills: List[str] 
    target_role: str