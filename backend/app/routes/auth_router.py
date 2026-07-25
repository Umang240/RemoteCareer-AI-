from fastapi import APIRouter, HTTPException, status

from app.models.auth_model import (
    SignupRequest,
    LoginRequest
)

from app.services.auth_service import (
    signup_user,
    login_user
)
from app.utils.response_utils import success_response

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(
    user: SignupRequest
):
    result = signup_user(user)
    if result.get("error"):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=result["error"],
        )
    return success_response(result["message"])


@router.post("/login")
async def login(
    user: LoginRequest
):
    result = login_user(user)
    if result.get("error"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=result["error"],
        )
    return success_response("Login successful", result)
