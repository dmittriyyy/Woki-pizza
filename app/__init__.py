from flask import Flask
from .extensions import db
from .routes import user

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    app.register_blueprint(user)  # нужно регистрировать blueprint

    db.init_app(app) # подключает базу к приложению
    with app.app_context():
        db.create_all()

    return app