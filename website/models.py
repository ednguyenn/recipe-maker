from . import db
from flask_login import UserMixin

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    instructions = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(50), unique= True)
    password = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    recipes = db.relationship('Recipe')