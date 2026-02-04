from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #Creacion de instancia unica

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    projects = db.relationship('Project', backref='author', lazy=True)

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    # Nueva columna para la imagen
    image_url = db.Column(db.String(255), nullable=True, default='default_img.png') 
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))