from fastapi import APIRouter, HTTPException, status
from app.models.user_model import User_profile
from app.database.db import users_collection
from bson import ObjectId, errors

router = APIRouter()


@router.post("/create-profile", status_code=status.HTTP_201_CREATED)
def create_profile(profile: User_profile):
    """Create a new user profile."""
    profile_data = profile.dict()
    users_collection.insert_one(profile_data)
    return {
        "message": "Profile created successfully"
    }


@router.get("/profiles")
def get_profiles():
    """Return all user profiles stored in MongoDB."""
    profiles = []
    for profile in users_collection.find():
        profile["_id"] = str(profile["_id"])
        profiles.append(profile)
    return profiles


@router.get("/profiles/{id}")
def get_profile(id: str):
    """Return a single user profile by MongoDB ObjectId."""
    try:
        object_id = ObjectId(id)
    except errors.InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid profile id format"
        )

    profile = users_collection.find_one({"_id": object_id})
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )

    profile["_id"] = str(profile["_id"])
    return profile


@router.put("/update-profile/{id}")
def update_profile(id: str, profile: User_profile):
    try:
        object_id = ObjectId(id)
    except errors.InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid profile id format"
        )

    result = users_collection.update_one(
        {"_id": object_id},
        {"$set": profile.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )

    return {
        "message": "Profile updated successfully"
    }


@router.delete("/delete-profile/{id}")
def delete_profile(id: str):
    try:
        object_id = ObjectId(id)
    except errors.InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid profile id format"
        )

    result = users_collection.delete_one({"_id": object_id})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )

    return {
        "message": "Profile deleted successfully"
    }
