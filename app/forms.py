from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    apellido = StringField('Apellido', validators=[DataRequired(), Length(min=2, max=100)])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    telefono = StringField('Teléfono', validators=[DataRequired(), Length(min=6, max=20)])
    canal = StringField('Canal de YouTube o TikTok', validators=[DataRequired(), Length(min=3, max=255)])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirmar = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('contraseña')])
    submit = SubmitField('Registrarse')
