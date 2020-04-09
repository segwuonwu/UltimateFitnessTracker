from flask import render_template , jsonify, request, json
from .models import Exercise, Equipment, Workout
from . import db

def get_workout():
    workout_list = Workout.query.all()
    results = [workout.as_dict() for workout in workout_list]
    return render_template('workouts.html', workout_list=workout_list)

def create_workout(**form_kwargs):
    new_workout = Workout(**form_kwargs)
    db.session.add(new_workout)
    db.session.commit()
    return render_template('workouts.html', new_workout=new_workout)

# def workout():
#     if request.method == 'GET':
#         pass
#     if request.method == 'POST':
#         name = request.form.get('name')
#         day = request.form.get('day')
#         sets = request.form.get('sets')
#         reps = request.form.get('reps')
#         exercise_id = request.form.get('exercise_id')
    
#     workouts = get_workout()

#     return render_template('workouts.html', workouts=workouts)
    
