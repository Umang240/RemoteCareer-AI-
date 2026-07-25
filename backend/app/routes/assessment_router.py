from fastapi import APIRouter, Depends, status
from app.middleware.auth_middleware import get_current_user
from app.models.assessment_model import AssessmentRequest
from app.services.assessment_service import get_career_recommendations
from app.utils.response_utils import success_response

router = APIRouter(
    prefix="/assessment",
    tags=["Career Assessment"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/", status_code=status.HTTP_200_OK)
async def assess_career(data: AssessmentRequest):
    recommendations = get_career_recommendations(
        data.interests
    )

    return success_response(
        "Career recommendations generated successfully",
        {"recommended_roles": recommendations},
    )
