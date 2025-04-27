from src.database.config import Base
from sqlalchemy import Column, String, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime

class Kehadiran(Base):
    __tablename__ = 'kehadiran'

    id = Column(Integer, primary_key=True)
    mahasiswa_nim = Column(String(20), ForeignKey('mahasiswa.nim'), nullable=False)
    jadwal_id = Column(Integer, ForeignKey('jadwal_perkuliahan.id'),nullable=False)
    status = Column(String(20), nullable=False)  # contoh: 'Hadir', 'Terlambat', 'Tidak Hadir'
    waktu_scan = Column(DateTime, nullable=False)

    mahasiswa = relationship('Mahasiswa', back_populates='kehadiran')
    jadwal = relationship('JadwalPerkuliahan', back_populates='kehadiran')
