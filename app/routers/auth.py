from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.db import get_db
from app.models.user import User
from app.utils.security import get_password_hash, verify_pasword
from app.schemas.user import UserCreate, UserLogin
from app.utils.jwt import create_access_token

router = APIRouter()

@router.post("/register")
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    existing_user_name = db.query(User).filter(User.username == user_data.username).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email Already Register")
    
    hashed_password = get_password_hash(user_data.password)

    if existing_user_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User name already Exist")

    new_user = User(
        username = user_data.username,
        email = user_data.email,
        hashed_password = hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User register successfully"} 


@router.post("/login")
def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    if not user or not verify_pasword(user_data.password, user.hashed_password):
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}