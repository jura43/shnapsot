from email.policy import default
from website import db
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), unique=True)
    password = db.Column(db.Text)
    is_admin = db.Column(db.Boolean, default=0)