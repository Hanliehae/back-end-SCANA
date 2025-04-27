from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.database.models.mahasiswa import Mahasiswa
from src.app import SessionLocal

mahasiswa_bp = Blueprint('mahasiswa_bp', __name__)

# HANYA ADMIN YANG BOLEH CRUD
def admin_required():
    user = get_jwt_identity()
    if user['role'] != 'admin':
        abort(403, description="Hanya admin yang bisa mengakses resource ini")
    return True

# Create Mahasiswa
@mahasiswa_bp.route('/', methods=['POST'])
@jwt_required()
def create_mahasiswa():
    admin_required()
    data = request.get_json()

    session = SessionLocal()
    try:
        new_mahasiswa = Mahasiswa(
            nim=data['nim'],
            nama=data['nama'],
            email=data['email'],
            no_telepon=data.get('no_telepon')
        )
        new_mahasiswa.set_password(data['password'])  # Set password

        session.add(new_mahasiswa)
        session.commit()

        return jsonify({"message": "Mahasiswa berhasil dibuat"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"message": "Gagal membuat mahasiswa", "error": str(e)}), 500
    finally:
        session.close()

# List Mahasiswa
@mahasiswa_bp.route('/', methods=['GET'])
@jwt_required()
def list_mahasiswa():
    admin_required()
    session = SessionLocal()
    try:
        mahasiswa_list = session.query(Mahasiswa).all()
        result = []
        for mhs in mahasiswa_list:
            result.append({
                "nim": mhs.nim,
                "nama": mhs.nama,
                "email": mhs.email,
                "no_telepon": mhs.no_telepon
            })
        return jsonify(result), 200
    finally:
        session.close()

# Delete Mahasiswa
@mahasiswa_bp.route('/<nim>', methods=['DELETE'])
@jwt_required()
def delete_mahasiswa(nim):
    admin_required()
    session = SessionLocal()
    try:
        mahasiswa = session.query(Mahasiswa).get(nim)
        if not mahasiswa:
            return jsonify({"message": "Mahasiswa tidak ditemukan"}), 404

        session.delete(mahasiswa)
        session.commit()
        return jsonify({"message": "Mahasiswa berhasil dihapus"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"message": "Gagal menghapus mahasiswa", "error": str(e)}), 500
    finally:
        session.close()
