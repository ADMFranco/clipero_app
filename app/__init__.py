from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    secret = os.getenv("SECRET_KEY", "clavepor_defecto")
    print("🔐 SECRET_KEY desde entorno:", secret)
    
    # Configuración de la app
    app.config['SECRET_KEY'] = secret
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")  # Render lo asignará

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'main.login' #Redirige a login si el usuario no esta  registrado


    from .models import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    from .routes import main
    app.register_blueprint(main)

    return app
