from flask import Blueprint, render_template , jsonify, request, json, redirect
from .models import Exercise, Equipment, Workout
from . import db

def exercise():
    e_list = Exercise.query.all()
    results = [exercise.as_dict() for exercise in e_list]
    return render_template('exercises.html', e_list=e_list)

def add_exercise():
    print(f"🍑🍑")
    print(request.form)
    db.session.add(Exercise(
    name=request.form['name'],
    description=request.form['description'],
    muscles=request.form['muscles'],
    workout_id=Workout.query.filter_by(name=request.form['workout']).first().id
    ))
    db.session.commit()
    return redirect('exercise')

