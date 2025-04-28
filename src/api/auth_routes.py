# src/api/auth_routes.py

from flask import Blueprint, request, jsonify
from src.database.models.user import User
from src.database.models.mahasiswa import Mahasiswa
from src.app import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

# === Admin Register ===
@auth_bp.route('/admin/register', methods=['POST'])
def register_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username sudah terdaftar"}), 409

    new_admin = User(username=username, email=email)
    new_admin.set_password(password)
    db.session.add(new_admin)
    db.session.commit()

    return jsonify({"message": "Admin berhasil didaftarkan"}), 201

# === Admin Login ===
@auth_bp.route('/admin/login', methods=['POST'])
def login_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    admin = User.query.filter_by(username=username).first()

    if admin and admin.check_password(password):
        access_token = create_access_token(identity={"role": "admin", "id": admin.id})
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Username atau password salah"}), 401

# === Mahasiswa Register ===
@auth_bp.route('/mahasiswa/register', methods=['POST'])
def register_mahasiswa():
    data = request.get_json()
    nim = data.get('nim')
    nama = data.get('nama')
    email = data.get('email')
    no_telepon = data.get('no_telepon')
    password = data.get('password')
    
    if Mahasiswa.query.filter_by(email=email).first():
        return jsonify({"message": "Email sudah terdaftar"}), 409

    new_mhs = Mahasiswa(
        nim=nim,
        nama=nama,
        email=email,
        no_telepon=no_telepon
    )
    new_mhs.set_password(password)
    db.session.add(new_mhs)
    db.session.commit()

    return jsonify({"message": "Mahasiswa berhasil didaftarkan"}), 201

# === Mahasiswa Login ===
@auth_bp.route('/mahasiswa/login', methods=['POST'])
def login_mahasiswa():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    mahasiswa = Mahasiswa.query.filter_by(email=email).first()

    if mahasiswa and mahasiswa.check_password(password):
        access_token = create_access_token(identity={"role": "mahasiswa", "nim": mahasiswa.nim})
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Email atau password salah"}), 401
