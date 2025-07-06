from . import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    canal = db.Column(db.String(255), nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)  # Se guarda en hash

    def __repr__(self):
        return f"<Usuario {self.nombre} {self.apellido}>"
