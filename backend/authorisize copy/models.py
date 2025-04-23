from sqlalchemy import Column, Integer, String, Date
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone = Column(String, unique=True, index=True)
    birth_date = Column(Date)
    email = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True)

