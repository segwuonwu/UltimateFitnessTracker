from flask import Blueprint, render_template , jsonify, request, json
from flask_login import login_required, current_user
from . import db
from .models import Exercise, Equipment, Workout
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/exercise')
def exercise():
    e_list = Exercise.query.all()
    exercise = []
    for x in e_list:
        exercise.append({'name' : x.name, "description": x.description, "muscles":x.muscles, "equipment_id":x.equipment_id})
    return jsonify({'exercises': exercises})
    
@main.route('/exercise/equipment')
def equipment():
    euip_list = Equipment.query.all()
    equipment = []
    for x in equip_list:
        equipment.append({'name' : x.name})
    return jsonify({'equipment': equipment})
    
@main.route('/exercise/add_equip', methods=['POST'])
def add_equipment():
    data = request.get_json()
    print(data)
    new_equipment = Equipment(name=data["name"])
    db.session.add(new_equipment)
    db.session.commit()

    return "Done", 201

@main.route('/exercise/add', methods=['POST'])
def add_exercise():
    data = request.get_json()

    new_exercise = Exercise(name=data['name'], description=data['description'], muscles=data['muscles'],
    equipment=data['equipment_id'])
    db.session.add(new_exercise)
    db.session.commit()

    return "Done", 201

#@login_required
@main.route('/workouts')
def workout():
    workout_list = Exercise.query.all()
    workouts = []
    for x in workout_list:
        workous.append({'name' : x.name, "date": x.date, "sets": x.sets, "reps": x.reps, "exercerses_id" : x.exercerses_id})
    return jsonify({'workouts': workouts})

@main.route('/workouts/<edit>', methods=['GET', 'POST'])
def edit_workout():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

