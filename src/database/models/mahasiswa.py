from src.database.config import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class Mahasiswa(Base):
    __tablename__ = 'mahasiswa'

    nim = Column(String(20),  primary_key=True, nullable=False)
    nama = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    no_telepon = Column(String(20))
    password_hash = Column(String(128), nullable=False)
    foto_tangan_kanan = Column(String(255))  # path file
    foto_tangan_kiri = Column(String(255))

    kontrak = relationship('Kontrak', back_populates='mahasiswa')
    kehadiran = relationship('Kehadiran', back_populates='mahasiswa')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
