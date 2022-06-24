from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from utils.db import db

class Tarea(db.Model):
    id_tarea = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, foreign_key = True)
    titulo = db.Column(db.String(100))
    descripcion = db.Column(db.String(500))

    def __init__(self, id_usuario, titulo, descripcion):
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.descripcion = descripcion


