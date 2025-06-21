from flask import Blueprint, jsonify
from services.people_service import get_all_people, get_person_by_id
from dto.serializers import people_serializer

people_bp = Blueprint('people_bp', __name__)

@people_bp.route('/people', methods=['GET'])
def list_people():
    people = get_all_people()
    serialized = [people_serializer(p) for p in people]
    return jsonify({"results": serialized}), 200

@people_bp.route('/people/<int:person_id>', methods=['GET'])
def get_people(person_id):
    person = get_person_by_id(person_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404
    return jsonify(people_serializer(person)), 200