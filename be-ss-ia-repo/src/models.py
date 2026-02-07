from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False) # Añadido username
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    # Relación para saber qué proyectos subió el usuario
    projects = db.relationship('Project', backref='uploader', lazy=True)

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    authors = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    ai_type = db.Column(db.String(100))
    summary = db.Column(db.Text)
    methodology = db.Column(db.Text)
    repository_url = db.Column(db.String(255))
    
    # Nombre del archivo PDF (ej: reporte_123.pdf)
    pdf_path = db.Column(db.String(255), nullable=False)
    
    # Relación con el usuario
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Fecha de registro automática
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.title}>'