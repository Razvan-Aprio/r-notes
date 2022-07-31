from . import db # importing from the current package, import the db variable
from flask_login import UserMixin #flask module that helps us with users login
from sqlalchemy.sql import func #get current date and time for storing date-time info in notes

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #by specifing ForeignKey we must pass a valid id to this column (one object to many children)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
