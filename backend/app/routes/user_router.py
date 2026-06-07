from fastapi import APIRouter
from app.models.user_model import User_profile
from app.database.db import profiles_collection
from bson import ObjectId

router = APIRouter()


@router.post("/create-profile")
def create_profile(profile: User_profile):
    """This API create user profile."""
    profile_data = profile.dict()
    profiles_collection.insert_one(profile_data)

    return {
        "message": "Profile created successfully"
    }

@router.get("/profiles")
def get_profiles():
    """This API returns all user profiles stored in MongoDB."""
    profiles = []

    for profile in profiles_collection.find():
        profile["_id"] = str(profile["_id"])
        profiles.append(profile)

    return profiles


@router.put("/update-profile/{id}")
def update_profile(id: str, profile: User_profile):

    profiles_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": profile.dict()}
    )

    return {
        "message": "Profile updated successfully"
    }

@router.delete("/delete-profile/{id}")
def delete_profile(id: str):

    profiles_collection.delete_one(
        {"_id": ObjectId(id)}
    )

    return {
        "message": "Profile deleted successfully"
    }
