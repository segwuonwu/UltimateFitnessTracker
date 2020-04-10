from flask import render_template , jsonify, request, json, redirect
from .models import Exercise, Equipment, Workout
from . import db

def get_workout():
    workout_list = Workout.query.all()
    results = [workout.as_dict() for workout in workout_list]
    return render_template('workouts.html', workout_list=workout_list)

def create_workout():
    db.session.add(Workout(
    name=request.form['name'],
    day=request.form['day'],
    sets=request.form['sets'],
    reps=request.form['reps']
    ))
    db.session.commit()
    return redirect('workouts.html')

def show_workout():
    workout_list = Workout.query.all()
    results = [workout.as_dict() for workout in workout_list]
    return render_template('profile.html', workout_list=workout_list)

