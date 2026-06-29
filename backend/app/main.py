from fastapi import FastAPI
from app.database import db
from app.routes.user_router import router as profile_router
from app.routes.assessment_router import router as assessment_router
from app.routes.skill_gap_router import router as skill_gap_router
from app.routes.roadmap_router import router as roadmap_router
from app.routes.career_advisor_router import router as career_advisor_router


app = FastAPI()

app.include_router(profile_router)
app.include_router(assessment_router)
app.include_router(skill_gap_router)
app.include_router(roadmap_router)
app.include_router(career_advisor_router)

@app.get("/")
def home_page():
    return {
        "message" : "CareerGPT backend server is running"
    }
