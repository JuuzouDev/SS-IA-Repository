
import os
from dotenv import load_dotenv

# Lectura de .env
load_dotenv()

class Config:
    """Configuracion Base"""
    # Llave secreta para sesiones de Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-7944-fesc') 
    
    # Configuración de JWT
    # Si no existe JWT_SECRET_KEY en el .env, usa la SECRET_KEY por defecto
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', SECRET_KEY)
    JWT_ACCESS_TOKEN_EXPIRES = 3600 * 24  # 24 horas (Perfecto para desarrollo)

    # Base de Datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    # Configuración de Archivos PDF
    # Usamos rutas absolutas para evitar confusiones en el servidor
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'uploads', 'reports')
    
    # Tamaño máximo de archivo (16MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    @staticmethod
    def init_app(app):
        # Asegurar que la carpeta de carga exista al arrancar
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
            print(f"Directorio creado en: {Config.UPLOAD_FOLDER}")

class DevelopmentConfig(Config):
    DEBUG = True
    # Podrías añadir aquí una configuración de base de datos local si fuera distinta
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@localhost/repo_ia'

class ProductionConfig(Config):
    DEBUG = False
    # En producción, nunca permitas llaves por defecto
    # SESSION_COOKIE_SECURE = True
    # REMEMBER_COOKIE_HTTPONLY = True

# Diccionario para facilitar la selección en el __init__.py
config_options = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
