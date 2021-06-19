from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(150))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
