from flask import Blueprint, request, jsonify, current_app
from src.models import db
from sqlalchemy import text
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, get_jwt_identity

import os


projects_bp = Blueprint('projects', __name__)

#configuracion de la carpeta de almacenamiento de reportes
UPLOAD_FOLDER = 'static/uploads/reports'

@projects_bp.route('/load_projects', methods=['GET'])
def load_projects():
    #LOGICA PARA LA CARGA DE PROYECTOS
    try:
        #Llamado al SP
        query = text("call sp_get_all_projects();")
        result = db.session.execute(query).fetchall()

        #conversion de filas de BD a lista de diccionarios
        projects_list=[]

        for row in result:
            projects_list.append({
                "id": row[0],
                "title": row[1],
                "authors": row[2],
                "year": row[3],
                "ai_type": row[4],
                "summary": row[5],
                "methodology": row[6],
                "repository_url": row[7],
                "pdf_path": row[8],
                "created_at": row[9].strftime('%Y-%m-%d'),
                "user": row[10]
            })
        return jsonify({
            "status": "success",
            "data": projects_list
        }), 200
    except Exception as e: 
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    
@projects_bp.route('/<int:id>', methods=['GET'])
def get_project_by_id(id):
    try:
        query = text ("CALL sp_get_project_detail(:id)")
        result = db.session.execute(query, {"id": id}).fetchone()

        if not result:
            return jsonify({"status": "error", "message": "Proyecto no Encontrado"}), 404
        
        #Mapeo de columnas a diccionario
        project_data = {
            "id": result[0],
            "title": result[1], 
            "authors": result[2],
            "year": result[3], 
            "ai_type": result[4], 
            "summary": result[5],
            "methodology": result[6], 
            "repository_url": result[7],
            "pdf_path": result[8], 
            "user": result[9]
        }

        return jsonify({"status": "success", "data": project_data}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    


@projects_bp.route('/upload', methods=['POST'])
@jwt_required()  #El usuario debe estar logueado para subir un proyecto
def upload_project():

    #print("=== DATOS RECIBIDOS EN FLASK ===")
    #print("Form:", request.form)  # Imprime textos (title, authors, etc.)
    #print("Files:", request.files) # Imprime archivos (report)

    #Obntener id del usuario directamente del Token
    current_user_id =  get_jwt_identity()
    #Extraer datos del formulario FORMDATA
    # 2. Extraer datos del FormData
    title = request.form.get('title')
    authors = request.form.get('authors')
    year = request.form.get('year')
    ai_type = request.form.get('ai_type')
    summary = request.form.get('summary')
    methodology = request.form.get('methodology')
    repo_url = request.form.get('repository_url')

    #Manejo de archivo PDF
    pdf_file = request.files.get('report')
    #Mensaje de retorno en caso de archivo invalido
    if not pdf_file or not pdf_file.filename.endswith('.pdf'):
        return jsonify({"status": "error", "message": "Se requiere un archivo PDF válido"}), 400
    
    #Proceso de Almacenado
    try: 
        #Guardado de archivo PDF fisicamente
        filename = secure_filename(pdf_file.filename)
        #Uso de Current app para acceder a la configuracion de la carpeta
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        pdf_file.save(upload_path)

        #Insercion en base de datos mediante SP
    
        query = text("""CALL sp_insert_project(
                     :title, :authors, :year, :ai_type, :summary,
                     :methodology, :repo_url, :pdf_path, :user
                     )
                     """)

        params = {
            "title": title,
            "authors": authors,
            "year": year,
            "ai_type": ai_type,
            "summary": summary,
            "methodology": methodology,
            "repo_url": repo_url,
            "pdf_path": filename, 
            "user": current_user_id  # <--- ID recuperado del JWT
        }

        result =  db.session.execute(query, params).fetchone()
        db.session.commit()

        if result and result[0] == 1:
            return jsonify({"status": "success", "message": "Proyecto Guardado Correctamente"}), 201
        else:
            #si el SP retorna 0, se borra el archivo para no dejar Basura
            if os.path.exists(upload_path):
                os.remove(upload_path)
            return jsonify({"status":"Error", "message": "Registro rechazado por la base de datos"}), 500
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500
    

