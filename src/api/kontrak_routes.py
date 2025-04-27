from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.database.models.kontrak import Kontrak
from src.database.models.mahasiswa import Mahasiswa
from src.database.models.matakuliah import MataKuliah
from src.database.config import db
from src.utils.role_checker import admin_required

kontrak_bp = Blueprint('kontrak_bp', __name__, url_prefix='/kontrak')

# Tambahkan mahasiswa ke mata kuliah (buat kontrak baru)
@kontrak_bp.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_kontrak():
    data = request.get_json()
    mahasiswa_nim = data.get('mahasiswa_nim')
    mata_kuliah_id = data.get('mata_kuliah_id')

    if not mahasiswa_nim or not mata_kuliah_id:
        return jsonify({"message": "Mahasiswa NIM dan Mata Kuliah ID wajib diisi"}), 400

    mahasiswa = Mahasiswa.query.filter_by(nim=mahasiswa_nim).first()
    if not mahasiswa:
        return jsonify({"message": "Mahasiswa tidak ditemukan"}), 404

    mata_kuliah = MataKuliah.query.filter_by(id=mata_kuliah_id).first()
    if not mata_kuliah:
        return jsonify({"message": "Mata kuliah tidak ditemukan"}), 404

    # Cek kalau kontrak sudah ada
    existing = Kontrak.query.filter_by(mahasiswa_nim=mahasiswa_nim, mata_kuliah_id=mata_kuliah_id).first()
    if existing:
        return jsonify({"message": "Mahasiswa sudah dikontrak ke mata kuliah ini"}), 409

    kontrak = Kontrak(mahasiswa_nim=mahasiswa_nim, mata_kuliah_id=mata_kuliah_id)
    db.session.add(kontrak)
    db.session.commit()

    return jsonify({"message": "Kontrak berhasil dibuat"}), 201


# Ambil daftar kontrak (bisa filter by mata kuliah id)
@kontrak_bp.route('/', methods=['GET'])
@jwt_required()
@admin_required
def get_kontrak():
    mata_kuliah_id = request.args.get('mata_kuliah_id')

    query = Kontrak.query
    if mata_kuliah_id:
        query = query.filter_by(mata_kuliah_id=mata_kuliah_id)

    kontrak_list = query.all()

    result = []
    for k in kontrak_list:
        result.append({
            "id": k.id,
            "mahasiswa_nim": k.mahasiswa_nim,
            "mata_kuliah_id": k.mata_kuliah_id,
            "mahasiswa_nama": k.mahasiswa.nama if k.mahasiswa else None,
            "mata_kuliah_nama": k.mata_kuliah.nama_mk if k.mata_kuliah else None
        })

    return jsonify(result), 200


# Hapus kontrak berdasarkan ID
@kontrak_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_kontrak(id):
    kontrak = Kontrak.query.get(id)
    if not kontrak:
        return jsonify({"message": "Kontrak tidak ditemukan"}), 404

    db.session.delete(kontrak)
    db.session.commit()

    return jsonify({"message": "Kontrak berhasil dihapus"}), 200
