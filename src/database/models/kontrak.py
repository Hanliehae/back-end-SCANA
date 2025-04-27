from src.database.config import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Kontrak(Base):
    __tablename__ = 'kontrak'

    id = Column(Integer, primary_key=True)
    mahasiswa_nim = Column(String(20), ForeignKey('mahasiswa.nim'), nullable=False)
    mata_kuliah_id = Column(Integer, ForeignKey('mata_kuliah.id'), nullable=False)

    mahasiswa = relationship('Mahasiswa', back_populates='kontrak')
    mata_kuliah = relationship('MataKuliah', back_populates='kontrak')

