import os
from flask import Flask
from .extensions import db
from .routes.user import user
from .routes.main import main  

from .models.role import Role  # заменить потом на routes

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    app.register_blueprint(user)  # нужно регистрировать blueprint
    app.register_blueprint(main)  

    db.init_app(app)              # подключает базу к приложению
    with app.app_context():
        db.create_all()

    return app