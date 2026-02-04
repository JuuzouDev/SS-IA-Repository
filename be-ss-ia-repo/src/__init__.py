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

    #Inicializacion de Extenciones
    jwt.init_app(app)
    db.init_app(app)
    #configuracion de CORS
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials= True)

    #Registro de Blueprints
    
    #importacion
    from .routes.main import main_bp
    from .routes.auth import auth_bp
    
    #registro
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/be/auth')

    return app
