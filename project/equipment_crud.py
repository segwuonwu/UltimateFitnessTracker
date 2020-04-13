from flask import Blueprint, render_template , jsonify, request, json, flash, redirect
from .models import Exercise, Equipment, Workout
from . import db

def equipment():
    equip_list = Equipment.query.all()
    results = [equipment.as_dict() for equipment in equip_list]
    return render_template('equipment.html', equip_list=equip_list) 

def create_equipment():
    db.session.add(Equipment(
        name=request.form['name'],
        exercise_id=Exercise.query.filter_by(name=request.form['exercise']).first()
    ))
    db.session.commit()
    return redirect('equipments')

def delete_equipment(id):
    workout = equipment.query.get(id)
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return redirect('equipments')
    else:
        raise Exception('No workout found on that {}'.format(id))


