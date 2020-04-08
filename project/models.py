from . import db
from flask_login import UserMixin
from datetime import date

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, email="{self.email}", name="{slef.name}", password="{self.password}")'

class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String, nullable=False)
    muscles = db.Column(db.String(100), nullable=False)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipments.id'), nullable=False)
    equipments = db.relationship('Equipment',
        backref=db.backref('exercises', lazy=True))

    def __repr__(self):
        return f'Exercise(id={self.id}, name="{self.name}", description="{self.description}", muscles="{self.muscles}")'


class Equipment(db.Model):
    __tablename__ = 'equipments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Equipment(id={self.id}, name="{self.name}")'

class Workout(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    sets = db.Column(db.String(50), nullable=False)
    reps = db.Column(db.String(50), nullable=False)
    exercises_id = db.Column(db.Integer, db.ForeignKey(' exercises.id'), nullable=False)
    exercises = db.relationship('Exercise', lazy='subquery',
        backref=db.backref('workouts', lazy=True))

    def __repr__(self):
        return f'Workout(id={self.id}, name="{self.name}", date="{self.date}", sets="{self.sets}", reps="{self.reps}")'
