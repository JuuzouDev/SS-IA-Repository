from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .models import db #instancia de la DB desde Models
from .config import DevelopmentConfig #importacion de clase de Desarrollo

#Creacion de instancia JWT
jwt = JWTManager()

#Creacion de APP
def create_app():
    app = Flask(__name__)

    #Carga de las Configuraciones completa
    app.config.from_object(DevelopmentConfig)
    #inicializar carpeta de Archivos PDF
    DevelopmentConfig.init_app(app)
    #Inicializacion de Extenciones
    jwt.init_app(app)
    db.init_app(app)
    #configuracion de CORS
    CORS(app, resources={r"/*": {
    "origins": "http://localhost:8080",
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"] # Crucial para JWT
    }}, supports_credentials=True)

    ##########################
    # Administracion de BP's #
    ##########################
    
    #importacion
    from .routes.main import main_bp
    from .routes.auth import auth_bp
    from .routes.projects import projects_bp
    from .routes.assistant import assistant_bp
    
    #registro
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(projects_bp, url_prefix='/projects')
    app.register_blueprint(assistant_bp, url_prefix = '/assistant')


    return app
