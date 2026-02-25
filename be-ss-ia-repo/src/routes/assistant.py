from flask import Blueprint, request, jsonify
from src.models import db
from sqlalchemy import text
from flask_jwt_extended import jwt_required
from google import genai

import os 
###################################################################
#COnfiguracion de Consulta con Motor GEMINI#
###################################################################
#Configuracion de cliente GENAI
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#Union de Prompt del usuario con el contexto del asistente
def generate_response_assistant(user_query, context_proyect):
    #system promt para contexto del asistente 
    prompt_system = f"""Eres un asistente Virtual de un repositorio de proyectos de inteligencia artificial para la FES Cuautitlan.
     tu mision es orientar y formar a los alimnos sobre buenas practicas.
     INFORMACION DEL REPOSITORIO: 
     {context_proyect}
     Reglas:
     1.- Responde de forma amable y academica.
     2.- Si el alumno pregunta por un tema que no esta en el contexto, invitalo a proponer un proyecto
     3.- Prioriza el uso de la metodologia descrita en los proyectos
     """
    
    try: 
        gemini_response =  client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=[prompt_system, f"Pregunta del alumno: {user_query}"]
        )
        
        return gemini_response.text
    
    except Exception as e:
        # Depuracion de error especifica en la consola
        print(f"Error detallado en Gemini: {e}")
        return "Lo siento, mi motor de inteligencia artificial no pudo procesar la respuesta."

###################################################################
#Configuracion de Blueprint
###################################################################

assistant_bp = Blueprint('assistant', __name__)

@assistant_bp.route('/ask', methods = ['POST'])
@jwt_required()
def chat_endpoint():
    try:

        user_msg =  request.json.get('message')

        #Ejecutar SP para obtener "Memoria" del REPO 
        db_result = db.session.execute(text("CALL sp_get_assistant_context()"))
        proyects = db_result.fetchall()

        #Formatear contexto para Gemini
        context = ""
        for p in proyects:
            context += f"Proyecto: {p.titulo} | Tecnologías: {p.tipo_ia} | Resumen: {p.resumen}\n"

        #Obtener respuesta de motor GEMINI
        answer = generate_response_assistant(user_msg, context)
        #print(answer)
        return jsonify({"answer": answer}), 200
    
    except Exception as e: 
        #Log del Error
        print(f"Error en Assistant: {str(e)}")
        return jsonify({"Error": "Ocurrio un error al procesar la solicitud" }), 500

