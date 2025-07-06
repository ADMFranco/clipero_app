from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.validators import ValidationError
from .models import Usuario
from wtforms.fields import DateField

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    apellido = StringField('Apellido', validators=[DataRequired(), Length(min=2, max=100)])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    telefono = StringField('Teléfono', validators=[DataRequired(), Length(min=6, max=20)])
    canal = StringField('Canal de YouTube o TikTok', validators=[DataRequired(), Length(min=3, max=255)])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirmar = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('contraseña')])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class EspacioForm(FlaskForm):
    fecha_inicio = DateField('Fecha de inicio', validators=[DataRequired()], format='%Y-%m-%d')
    fecha_fin = DateField('Fecha de fin', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Crear espacio de trabajo')
