from pydantic import BaseModel

class RoadmapRequest(BaseModel):
    target_role: str