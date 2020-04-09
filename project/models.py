from . import db
from flask_login import UserMixin

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
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id', ondelete='SET NULL'))
    equipments = db.relationship('Equipment', backref='equipment_name')

    def __repr__(self):
        return f'Exercise(id={self.id}, name="{self.name}", description="{self.description}", muscles="{self.muscles}", equipments="{self.equipments}")'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Equipment(db.Model):
    __tablename__ = 'equipments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    exercises = db.relationship('Exercise', backref='exercise_name')
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id', ondelete='SET NULL'))

    def __repr__(self):
        return f'Equipment(id={self.id}, name="{self.name}")'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Workout(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    day = db.Column(db.String(50), nullable=False)
    sets = db.Column(db.String(50), nullable=False)
    reps = db.Column(db.String(50), nullable=False)
    exercises = db.relationship('Exercise', backref='workout_exercise')

    def __repr__(self):
        return f'Workout(id={self.id}, name="{self.name}", day="{self.day}", sets="{self.sets}", reps="{self.reps}, exercise="self.exercises")'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
