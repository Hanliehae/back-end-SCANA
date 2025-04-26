from src.database.config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class Mahasiswa(Base):
    __tablename__ = 'mahasiswa'

    nim = Column(String(20), primary_key=True)
    no_telepon = Column(String(20))
    
    foto_tangan_kiri = Column(String(200))
    foto_tangan_kanan = Column(String(200))
    foto_wajah = Column(String(200))
