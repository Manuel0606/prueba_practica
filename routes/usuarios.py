from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.usuario import Usuario
from utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash
# from tareas import id_usuario

usuarios = Blueprint('usuarios', __name__)


@usuarios.route('/')
def inicio():
    usuarios = Usuario.query.all()
    return render_template('iniciar_sesion.html', usuarios = usuarios)


@usuarios.route('/registrar', methods=['POST','GET'])
def registrar_usuario():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        password = request.form['password']

        password_cifrada = generate_password_hash(password, 'pbkdf2:sha256', 30)

        nuevo_usuario = Usuario(nombre, apellidos, correo, password_cifrada)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash("Usuario Creado!!")

        return redirect(url_for('usuarios.inicio'))

    return render_template('crear_usuario.html')


@usuarios.route('/iniciarSesion', methods = ['POST', 'GET'])
def editar_usuario():
    # usuario = Usuario.query.get(id)
    usuarios = Usuario.query.all()

    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        for usuario in usuarios:
            print(correo)
            print(usuario.correo)
            print(check_password_hash(usuario.password, password))
            if usuario.correo == correo and check_password_hash(usuario.password, password):
                flash("Usuario Correcto!!")
                return redirect(url_for('tareas.inicio'))
            
        flash("Usuario Incorrecto!!")
        return redirect(url_for('usuarios.inicio'))

    return redirect(url_for('usuarios.inicio'))

