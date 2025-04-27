from flask_jwt_extended import JWTManager

# di dalam create_app()
src.config["JWT_SECRET_KEY"] = "super-secret-key"  # ganti ini dengan kunci rahasiamu
jwt = JWTManager(src)
