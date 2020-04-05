from . import db
from flask_login import UserMixin

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, email="{self.email}", name="{slef.name}", password="{self.password}")'

