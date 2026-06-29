from pydantic import BaseModel, Field

class RoadmapRequest(BaseModel):
    target_role: str = Field(..., min_length=1)