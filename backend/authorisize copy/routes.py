from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .models import User
from .shemas import RegisterRequest, RegisterResponse
from .security import get_password_hash
from .database import get_db
from sqlalchemy import select


def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    user = db.execute(
        select(User).where(
            User.full_name == request.full_name,
            User.phone == request.phone,
            User.birth_date == request.birth_date
        )
    ).scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found in CSV records")

    if user.email or user.hashed_password:
        raise HTTPException(status_code=400, detail="User already registered")

    user.email = request.email
    user.hashed_password = get_password_hash(request.password)
    db.commit()

    return RegisterResponse(message="Registration successful")