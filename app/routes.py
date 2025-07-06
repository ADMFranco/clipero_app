from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import RegistroForm
from .models import Usuario
from . import db
from werkzeug.security import generate_password_hash

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
