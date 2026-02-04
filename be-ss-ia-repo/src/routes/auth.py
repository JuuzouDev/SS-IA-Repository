from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from src.models import db, User # Importar Instancia de la BD y el user
from sqlalchemy import text 
from flask_jwt_extended import create_access_token
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = data.get('user')
    password = data.get('password')
    

    try:
        # Llamamos al procedimiento almacenado usando text()
        # El método .params() pasa los argumentos de forma segura contra SQL Injection
        #llamado al SP 
        query = text("CALL sp_validate_login(:user)")
        result = db.session.execute(query, {"user": user}).fetchone()

        # Result contiene los datos traidos del SP
            #Estructura de datos traidos
            # (id: 0, username: 1, email: 2, password_hash: 3, role: 4)

        if result:
            db_password_hash = result[3]
            
            if check_password_hash(db_password_hash, password):
                #Creacion del Token de login
                access_token = create_access_token(identity=str(result[0]), additional_claims = {"role": result[3]} )

                return jsonify({
                    "status": "success",
                    "token" : access_token,
                    "user": {"username": result[1], "role": result[3]}
                }), 200
        
        return jsonify({"message": "Credenciales incorrectas"}), 401

    except Exception as e:
        print(f"Error en la BD: {str(e)}")
        return jsonify({"message": "Error interno del servidor"}), 500

