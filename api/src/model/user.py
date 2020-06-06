'''
User administration
'''

from config import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    first_name = db.Column(db.String(128), unique=False, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password
