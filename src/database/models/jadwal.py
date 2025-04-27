from src.database.config import Base
from sqlalchemy import Column, String, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship


class JadwalPerkuliahan(Base):
    __tablename__ = 'jadwal_perkuliahan'

    id = Column(Integer, primary_key=True)
    mata_kuliah_id = Column(Integer, ForeignKey('mata_kuliah.id'), nullable=False)
    pertemuan_ke = Column(Integer, nullable=False)
    tanggal = Column(Date, nullable=False)
    jam_mulai = Column(Time, nullable=False)
    jam_selesai = Column(Time, nullable=False)

    mata_kuliah = relationship('MataKuliah', back_populates='jadwal')
    kehadiran = relationship('Kehadiran', back_populates='jadwal')
