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

def sunday():
    work = Workout.query.all()
    if work:
        results = [workout.as_dict() for workout in work]
        return render_template('profile.html', work=results)
    else:
        raise Exception('No workout found')

def update_workout():
    print(request.form)
    return redirect('workouts.html')


