import os
from flask import Flask
from .extensions import db, migrate
from .routes.user import user
from .routes.main import main  
from .routes.auth import auth

from .models.role import Role  # заменить потом на routes

def create_app():
    app = Flask(__name__, template_folder='../app/templates', static_folder='../app/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    app.register_blueprint(user)  # нужно регистрировать blueprint
    app.register_blueprint(main)  
    app.register_blueprint(auth)  

    db.init_app(app)              # подключает базу к приложению
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()

    return app