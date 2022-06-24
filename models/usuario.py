from tabnanny import check
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from utils.db import db
from werkzeug.security import check_password_hash

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    password = db.Column(db.String(500))

    def __init__(self, nombre, apellidos, correo, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.password = password
    

