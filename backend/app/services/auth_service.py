from app.database.db import users_collection
from app.utils.auth_utils import (
    hash_password,
    verify_password,
    create_access_token
)


def signup_user(user):

    existing_user = users_collection.find_one(
        {"email": user.email}
    )

    if existing_user:
        return {
            "message": "Email already exists"
        }

    hashed_password = hash_password(
        user.password
    )

    user_data = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }

    users_collection.insert_one(
        user_data
    )

    return {
        "message": "User registered successfully"
    }

def login_user(user):

    db_user = users_collection.find_one(
        {"email": user.email}
    )

    if not db_user:
        return {
            "message": "Invalid credentials"
        }

    if not verify_password(
        user.password,
        db_user["password"]
    ):
        return {
            "message": "Invalid credentials"
        }

    token = create_access_token(
        {
            "sub": db_user["email"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }