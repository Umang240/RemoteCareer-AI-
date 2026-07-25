from fastapi import APIRouter, Depends, HTTPException, status

from app.middleware.auth_middleware import get_current_user
from app.models.roadmap_model import RoadmapRequest
from app.services.roadmap_service import generate_roadmap
from app.utils.response_utils import success_response

router = APIRouter(
    prefix="/roadmap",
    tags=["Learning Roadmap"],
    dependencies=[Depends(get_current_user)]
)


@router.post("/")
async def get_roadmap(data: RoadmapRequest):

    result = generate_roadmap(
        data.target_role
    )

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=result["error"],
        )
    return success_response("Learning roadmap generated successfully", result)
