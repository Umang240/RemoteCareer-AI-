from fastapi import APIRouter
from app.models.career_advisor_model import CareerAdviceRequest
from app.services.career_advisor_service import generate_career_advice

router = APIRouter(
    prefix="/career-advice",
    tags=["Career Advisor"]
)

@router.post("/")
async def get_career_advice(data: CareerAdviceRequest):
    return generate_career_advice(
        data.education,
        data.skills,
        data.target_role
    )