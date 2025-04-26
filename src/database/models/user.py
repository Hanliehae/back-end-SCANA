from sqlalchemy import Column, Integer, String
from src.database.config import Base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nama_lengkap = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
