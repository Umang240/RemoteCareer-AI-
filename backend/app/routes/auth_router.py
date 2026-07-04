from fastapi import APIRouter

from app.models.auth_model import (
    SignupRequest,
    LoginRequest
)

from app.services.auth_service import (
    signup_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
async def signup(
    user: SignupRequest
):
    return signup_user(user)


@router.post("/login")
async def login(
    user: LoginRequest
):
    return login_user(user)