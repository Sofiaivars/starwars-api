from flask import Blueprint, jsonify
from services.vehicle_service import get_all_vehicles, get_vehicle_by_id
from dto.serializers import vehicle_serializer

vehicle_bp = Blueprint('vehicle_bp', __name__)

@vehicle_bp.route('/vehicles', methods=['GET'])
def list_vehicles():
    vehicles = get_all_vehicles()
    serialized = [vehicle_serializer(v) for v in vehicles]
    return jsonify({"results": serialized}), 200

@vehicle_bp.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = get_vehicle_by_id(vehicle_id)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    return jsonify(vehicle_serializer(vehicle)), 200
