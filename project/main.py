from flask import Blueprint, render_template , jsonify, request, json
from flask_login import login_required, current_user
from . import db
from .models import Exercise, Equipment, Workout
from .workout_crud import get_workout, create_workout
from .exercise_crud import exercise, add_exercise
from .equipment_crud import equipment, create_equipment

import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
# @login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/exercise', methods=["GET", "POST"])
def get_exercise():
    if request.method == 'GET':
        return exercise()
    if request.method == "POST":
        print(f"🍑 Here on add exercise🎖")
        return add_exercise()

    
@main.route('/equipments', methods=["GET", "POST"])
def get_equipment():
    if request.method == 'GET':
        return equipment()
    if request.method == 'POST':
        return create_equipment()


#@login_required
@main.route('/workouts', methods=["GET", "POST"])
def workouts():
    if request.method == 'GET':
        return get_workout()
    if request.method == 'POST':
        return create_workout()

