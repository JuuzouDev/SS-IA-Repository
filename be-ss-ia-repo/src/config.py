import os
from dotenv import load_dotenv

#Lectura de .env
load_dotenv()

class Config:
    """Configuracion Base para Desarrollo"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-key-for-dev')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    #Configuracion de Archivos PDF
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads', 'reports')
    
    # Tamaño máximo de archivo (Ejemplo: 16MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    @staticmethod
    def init_app(app):
        #Crear la carpeta de archivos pdf si no existe
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    
    #AGREGAR CAMBIOS DE AMBIENTE PRODUCTIVO


