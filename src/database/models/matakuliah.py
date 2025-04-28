from src.database.config import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class MataKuliah(Base):
    __tablename__ = 'mata_kuliah'

    id = Column(Integer, primary_key=True)
    kode_mk = Column(String(20), nullable=False, unique=True)
    nama_mk = Column(String(100), nullable=False)
    semester = Column(String(10), nullable=False)  # 'Ganjil' atau 'Genap'
    tahun_akademik = Column(String(4), nullable=False)  # contoh: 2025
    kelas = Column(String(5), nullable=False)

    kontrak = relationship('Kontrak', back_populates='mata_kuliah')
    jadwal = relationship('JadwalPerkuliahan', back_populates='mata_kuliah')
