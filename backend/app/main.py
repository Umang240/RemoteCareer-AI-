import logging
import os
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.database import db
from app.routes.user_router import router as profile_router
from app.routes.assessment_router import router as assessment_router
from app.routes.skill_gap_router import router as skill_gap_router
from app.routes.roadmap_router import router as roadmap_router
from app.routes.career_advisor_router import router as career_advisor_router
from app.routes.auth_router import (router as auth_router)
from app.utils.response_utils import error_response, success_response


app = FastAPI()

ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS",
        "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173"
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger(__name__)

app.include_router(profile_router)
app.include_router(assessment_router)
app.include_router(skill_gap_router)
app.include_router(roadmap_router)
app.include_router(career_advisor_router)
app.include_router(auth_router)


@app.exception_handler(HTTPException)
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(_: Request, exc: StarletteHTTPException):
    """Return application and authentication errors in the API envelope."""
    message = exc.detail if isinstance(exc.detail, str) else "Request failed"
    data = None if isinstance(exc.detail, str) else exc.detail
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(message, data),
        headers=exc.headers,
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=error_response("Validation failed", exc.errors()),
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(_: Request, exc: Exception):
    """Avoid leaking internals while keeping unexpected errors consistent."""
    logger.exception("Unhandled API error", exc_info=exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=error_response("An unexpected server error occurred"),
    )

@app.get("/")
def home_page():
    return success_response("CareerGPT backend server is running")
