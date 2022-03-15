from source import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id_user):
    return User.query.get(int(id_user))

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)  # primary_key define o usuário como único
    username = database.Column(database.String, nullable=False)  # nullable serve para não ser vazio
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    profile_pic = database.Column(database.String, default='default.jpg', nullable=False)
