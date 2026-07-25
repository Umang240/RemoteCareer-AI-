from fastapi import APIRouter, Depends, HTTPException, status
from app.middleware.auth_middleware import get_current_user
from app.models.career_advisor_model import CareerAdviceRequest
from app.services.career_advisor_service import generate_career_advice
from app.utils.response_utils import success_response

router = APIRouter(
    prefix="/career-advice",
    tags=["Career Advisor"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/")
async def get_career_advice(data: CareerAdviceRequest):
    result = generate_career_advice(
        data.education,
        data.skills,
        data.target_role
    )
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=result["error"],
        )
    return success_response("Career advice generated successfully", result)
