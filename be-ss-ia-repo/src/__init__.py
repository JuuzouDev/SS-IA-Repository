from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    CORS(app)

    # Importar los Blueprints
    from .routes.main import main_bp
    from .routes.auth import auth_bp
    #from .routes.assistant import assistant_bp

    # Registrar los Blueprints con un prefijo de URL
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    #app.register_blueprint(assistant_bp, url_prefix='/api/assistant')

    return app