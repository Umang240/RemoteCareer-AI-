from fastapi import APIRouter, HTTPException, status
from app.models.assessment_model import AssessmentRequest
from app.services.assessment_service import get_career_recommendations

router = APIRouter(
    prefix="/assessment",
    tags=["Career Assessment"]
)

@router.post("/", status_code=status.HTTP_200_OK)
async def assess_career(data: AssessmentRequest):
    recommendations = get_career_recommendations(
        data.interests
    )

    return {
        "recommended_roles": recommendations
    }