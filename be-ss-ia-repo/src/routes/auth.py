from flask import Blueprint, request, jsonify

#Definicion del blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = data.get('user')
    psw = data.get('psw')

    #Logica de validacion de credenciales


