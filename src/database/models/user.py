from flask_sqlalchemy import SQLAlchemy
from src.database.config import Base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    email = Column(String(100), unique=True)
    role = Column(String(20), default='admin')  # Kalau mau lebih aman

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
