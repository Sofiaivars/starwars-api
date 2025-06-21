from flask import Blueprint, jsonify
from services.planet_service import get_all_planets, get_planet_by_id
from dto.serializers import planet_serializer

planet_bp = Blueprint('planet_bp', __name__)

@planet_bp.route('/planets', methods=['GET'])
def list_planets():
    planets = get_all_planets()
    serialized = [planet_serializer(p) for p in planets]
    return jsonify({"results": serialized}), 200

@planet_bp.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = get_planet_by_id(planet_id)
    if not planet:
        return jsonify({"error": "Planet not found"}), 404
    return jsonify(planet_serializer(planet)), 200