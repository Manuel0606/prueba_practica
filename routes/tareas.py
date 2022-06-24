from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.tarea import Tarea
from utils.db import db


tareas = Blueprint('tareas', __name__)


@tareas.route('/tareas')
def inicio():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas = tareas)


@tareas.route('/crear', methods=['POST'])
def crear_tarea():
    id_usuario = request.form['id_usuario']
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']

    nueva_tarea = Tarea(id_usuario, titulo, descripcion)

    db.session.add(nueva_tarea)
    db.session.commit()

    flash("Tarea Creada!!")

    return redirect(url_for('tareas.inicio'))


@tareas.route('/editar/<id>', methods = ['POST', 'GET'])
def editar_tarea(id):
    tarea = Tarea.query.get(id)

    if request.method == 'POST':
        tarea.id_usuario = request.form["id_usuario"]
        tarea.titulo = request.form["titulo"]
        tarea.descripcion = request.form["descripcion"]
        db.session.commit()

        flash("Tarea Actualizada!!")

        return redirect(url_for('tareas.inicio'))

    return render_template('actualizar.html', tarea=tarea)


@tareas.route('/eliminar/<id>')
def eliminar_tarea(id):
    tarea = Tarea.query.get(id)
    db.session.delete(tarea)
    db.session.commit()

    flash("Tarea Eliminada!!")

    return redirect(url_for('tareas.inicio'))

