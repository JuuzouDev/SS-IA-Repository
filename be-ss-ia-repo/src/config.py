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

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    
    #AGREGAR CAMBIOS DE AMBIENTE PRODUCTIVO


