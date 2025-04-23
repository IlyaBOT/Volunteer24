from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Base, engine, User
from  .shemas import RegisterRequest, RegisterResponse
from .database import SessionLocal, load_users_from_csv, get_db
from .security import get_password_hash
from .routes import register_user

Base.metadata.create_all(bind=engine)
load_users_from_csv()

app = FastAPI()

app.post("/register", response_model=RegisterResponse)(register_user)

