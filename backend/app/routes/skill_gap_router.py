from fastapi import APIRouter, Depends, HTTPException, status

from app.middleware.auth_middleware import get_current_user
from app.models.skill_gap_model import SkillGapRequest
from app.services.skill_gap_service import analyze_skill_gap
from app.utils.response_utils import success_response

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

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=result["error"],
        )
    return success_response("Skill gap analysis completed successfully", result)
