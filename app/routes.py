from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import RegistroForm
from .forms import EspacioForm
from .forms import LoginForm
from .models import Usuario
from .models import EspacioTrabajo
from . import db
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Bienvenido a la plataforma de cliperos"

@main.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        nuevo_usuario = Usuario(
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            correo=form.correo.data,
            telefono=form.telefono.data,
            canal=form.canal.data,
            contraseña=generate_password_hash(form.contraseña.data)
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('¡Registro exitoso! Ya puedes iniciar sesión.', 'success')
        return redirect(url_for('main.index'))
    return render_template('registro.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(correo=form.correo.data).first()
        if usuario and check_password_hash(usuario.contraseña, form.contraseña.data):
            login_user(usuario)
            flash('¡Has iniciado sesión correctamente!', 'success')
            return redirect(url_for('main.panel'))
        else:
            flash('Correo o contraseña incorrectos', 'danger')
    return render_template('login.html', form=form)

@main.route('/panel')
@login_required
def panel():
    return f"Bienvenido {current_user.nombre}, este es tu panel de clipero."

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('main.index'))

@main.route('/crear_espacio', methods=['GET', 'POST'])
@login_required
def crear_espacio():
    form = EspacioForm()
    if form.validate_on_submit():
        nuevo_espacio = EspacioTrabajo(
            usuario_id=current_user.id,
            fecha_inicio=form.fecha_inicio.data,
            fecha_fin=form.fecha_fin.data
        )
        db.session.add(nuevo_espacio)
        db.session.commit()
        flash('Espacio de trabajo creado correctamente.', 'success')
        return redirect(url_for('main.panel'))
    return render_template('crear_espacio.html', form=form)
