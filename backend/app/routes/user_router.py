from fastapi import APIRouter, Depends, HTTPException, status
from app.models.user_model import User_profile
from app.database.db import profiles_collection
from app.middleware.auth_middleware import get_current_user
from bson import ObjectId, errors

router = APIRouter(dependencies=[Depends(get_current_user)])


def _parse_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except errors.InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid profile id format"
        )


def _get_owned_profile(object_id: ObjectId, user_id: str):
    """Fetch a profile and confirm it belongs to the current user."""
    profile = profiles_collection.find_one({"_id": object_id})

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )

    if profile.get("user_id") != user_id:
        # 404 instead of 403 so we don't confirm the id exists to a non-owner
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )

    return profile


@router.post("/create-profile", status_code=status.HTTP_201_CREATED)
def create_profile(
    profile: User_profile,
    current_user=Depends(get_current_user)
):
    """Create a profile owned by the current authenticated user."""
    user_id = str(current_user["_id"])

    if profiles_collection.find_one({"user_id": user_id}):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Profile already exists for this user"
        )

    profile_data = profile.dict()
    profile_data["user_id"] = user_id

    result = profiles_collection.insert_one(profile_data)

    return {
        "message": "Profile created successfully",
        "profile_id": str(result.inserted_id)
    }


@router.get("/profile/me")
def get_my_profile(current_user=Depends(get_current_user)):
    """Return the profile belonging to the current authenticated user."""
    profile = profiles_collection.find_one(
        {"user_id": str(current_user["_id"])}
    )

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found for this user"
        )

    profile["_id"] = str(profile["_id"])
    return profile


@router.get("/profiles/{id}")
def get_profile(id: str, current_user=Depends(get_current_user)):
    """Return a single profile by id, if it belongs to the current user."""
    profile = _get_owned_profile(
        _parse_object_id(id),
        str(current_user["_id"])
    )
    profile["_id"] = str(profile["_id"])
    return profile


@router.put("/update-profile/{id}")
def update_profile(
    id: str,
    profile: User_profile,
    current_user=Depends(get_current_user)
):
    object_id = _parse_object_id(id)
    _get_owned_profile(object_id, str(current_user["_id"]))

    profiles_collection.update_one(
        {"_id": object_id},
        {"$set": profile.dict()}
    )

    return {
        "message": "Profile updated successfully"
    }


@router.delete("/delete-profile/{id}")
def delete_profile(id: str, current_user=Depends(get_current_user)):
    object_id = _parse_object_id(id)
    _get_owned_profile(object_id, str(current_user["_id"]))

    profiles_collection.delete_one({"_id": object_id})

    return {
        "message": "Profile deleted successfully"
    }