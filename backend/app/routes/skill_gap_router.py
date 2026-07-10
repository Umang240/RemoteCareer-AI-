from fastapi import APIRouter, Depends

from app.middleware.auth_middleware import get_current_user
from app.models.skill_gap_model import SkillGapRequest
from app.services.skill_gap_service import analyze_skill_gap

router = APIRouter(
    prefix="/skill-gap",
    tags=["Skill Gap Analysis"],
    dependencies=[Depends(get_current_user)]
)


@router.post("/")
async def get_skill_gap(data: SkillGapRequest):

    result = analyze_skill_gap(
        data.target_role,
        data.current_skills
    )

    return result