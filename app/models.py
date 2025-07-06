from . import db
from flask_login import UserMixin
from datetime import date

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
    
class EspacioTrabajo(db.Model):
    __tablename__ = 'espacio_trabajo'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<EspacioTrabajo {self.fecha_inicio} - {self.fecha_fin}>"
    
class Clip(db.Model):
    __tablename__ = 'clips'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    vistas = db.Column(db.Integer, default=0)
    fecha_subida = db.Column(db.Date, default=date.today)

    espacio_id = db.Column(db.Integer, db.ForeignKey('espacio_trabajo.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return f"<Clip {self.titulo}>"

