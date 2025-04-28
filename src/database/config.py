from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from dotenv import load_dotenv
import os

# Load variabel dari .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')  # Sama aja, lebih simpel
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ambil DATABASE_URL dari environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Buat engine SQLAlchemy
engine = create_engine(DATABASE_URL)

# Session dan Base ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

db_session=scoped_session(SessionLocal)
Base.query= db_session.query_property()