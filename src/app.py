# src/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    jwt.init_app(app)

    # import dan register blueprint
    from src.api.auth_routes import auth_bp
    from src.api.mahasiswa_routes import mahasiswa_bp
    # from src.api.kontrak_routes import kontrak_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(mahasiswa_bp, url_prefix="/mahasiswa")
    # app.register_blueprint(kontrak_bp)

    return app

# INI PENTING!! untuk jalanin server
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)