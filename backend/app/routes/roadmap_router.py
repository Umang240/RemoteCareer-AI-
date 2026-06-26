from fastapi import APIRouter

from app.models.roadmap_model import RoadmapRequest
from app.services.roadmap_service import generate_roadmap

router = APIRouter(
    prefix="/roadmap",
    tags=["Learning Roadmap"]
)


@router.post("/")
async def get_roadmap(data: RoadmapRequest):

    result = generate_roadmap(
        data.target_role
    )

    return result