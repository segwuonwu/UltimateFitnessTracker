from flask import Blueprint, render_template , jsonify, request, json
from .models import Exercise, Equipment, Workout

def exercise():
    e_list = Exercise.query.all()
    results = [exercise.as_dict() for exercise in e_list]
    return render_template('exercises.html', e_list=e_list)


def add_exercise():
    data = request.get_json()
    new_exercise = Exercise(name=data['name'], description=data['description'], muscles=data['muscles'])
    db.session.add(new_exercise)
    db.session.commit()

    return "Done", 201


