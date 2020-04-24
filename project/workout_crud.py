from flask import render_template, jsonify, request, json, redirect
from flask_login import  current_user
from .models import Exercise, Equipment, Workout
from . import db

def get_workout():
    workout_list = Workout.query.all()
    results = [workout.as_dict() for workout in workout_list]
    return render_template('workouts.html', name=current_user.name,  workout_list=workout_list)

def create_workout():
    db.session.add(Workout(
    name=request.form['name'],
    day=request.form['day'],
    sets=request.form['sets'],
    reps=request.form['reps']
    ))
    db.session.commit()
    return redirect('workouts')

def update_workout():
    return render_template('update.html')


