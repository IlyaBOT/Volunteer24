from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated
from datetime import date

PasswordStr = Annotated[str, StringConstraints(min_length=6)]

class RegisterRequest(BaseModel):
    full_name: str
    phone: str
    email: EmailStr
    birth_date: date
    password: PasswordStr

class RegisterResponse(BaseModel):
    message: str
