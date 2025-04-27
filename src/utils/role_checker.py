from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from functools import wraps
from src.database.models.user import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        user = User.query.filter_by(id=current_user).first()
        if user and user.role == 'admin':
            return fn(*args, **kwargs)
        else:
            return jsonify({"message": "Akses hanya untuk admin"}), 403
    return wrapper
