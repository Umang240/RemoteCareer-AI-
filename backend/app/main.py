from fastapi import FastAPI
from app.database import db
from app.routes.user_router import router as profile_router
app = FastAPI()

app.include_router(profile_router)


@app.get("/")
def home_page():
    return {
        "message" : "CareerGPT backend server is running"
    }
