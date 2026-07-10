from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import get_current_user
from app.models.career_advisor_model import CareerAdviceRequest
from app.services.career_advisor_service import generate_career_advice

router = APIRouter(
    prefix="/career-advice",
    tags=["Career Advisor"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/")
async def get_career_advice(data: CareerAdviceRequest):
    return generate_career_advice(
        data.education,
        data.skills,
        data.target_role
    )

    