from flask import Blueprint, render_template , jsonify, request, json
from .models import Exercise, Equipment, Workout

def equipment():
    equip_list = Equipment.query.all()
    results = [equipment.as_dict() for equipment in equip_list]
    return jsonify(results)
    
def add_equipment():
    data = request.get_json()
    print(data)
    new_equipment = Equipment(name=data["name"])
    db.session.add(new_equipment)
    db.session.commit()

    return "Done", 201