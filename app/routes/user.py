from flask import Blueprint
from ..models.user import User
from ..extensions import db

user = Blueprint('user', __name__)

@user.route('/user/<username>')
def create_user(username):
    user = User(username = username)
    db.session.add(user)
    db.session.commit()
    return f"Пользователь {username} создан"