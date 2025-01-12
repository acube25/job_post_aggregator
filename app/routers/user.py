from fastapi import APIRouter, Depends

from app.models.user import User
from app.utils.jwt import get_current_user
from app.schemas.user import UserProfile

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/me", response_model=UserProfile)
def read_user_profile(current_user: User = Depends(get_current_user)):
    return UserProfile(
        username = current_user.username,
        email = current_user.email,
        id = current_user.id
    )