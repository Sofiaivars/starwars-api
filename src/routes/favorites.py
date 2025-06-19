from flask import Blueprint, jsonify, request
from services.favorite_service import (
    get_favorites_by_user,
    add_favorite_planet,
    add_favorite_people,
    remove_favorite_planet,
    remove_favorite_people
)

favorites_bp = Blueprint('favorites', __name__, url_prefix='/favorites')

CURRENT_USER_ID = 1

@favorites_bp.route('/user', methods=['GET'])
def list_favorites():
    favorites = get_favorites_by_user(CURRENT_USER_ID)
    return jsonify(favorites), 200

@favorites_bp.route('/planet/<int:planet_id>', methods=['POST'])
def add_planet_favorite(planet_id):
    fav = add_favorite_planet(CURRENT_USER_ID, planet_id)
    if not fav:
        return jsonify({"message": "Favorite already exists"}), 400
    return jsonify(fav), 201

@favorites_bp.route('/people/<int:people_id>', methods=['POST'])
def add_people_favorite(people_id):
    fav = add_favorite_people(CURRENT_USER_ID, people_id)
    if not fav:
        return jsonify({"message": "Favorite already exists"}), 400
    return jsonify(fav), 201

@favorites_bp.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_favorite(planet_id):
    success = remove_favorite_planet(CURRENT_USER_ID, planet_id)
    if success:
        return jsonify({"message": "Favorite removed"}), 200
    return jsonify({"message": "Favorite not found"}), 404

@favorites_bp.route('/people/<int:people_id>', methods=['DELETE'])
def delete_people_favorite(people_id):
    success = remove_favorite_people(CURRENT_USER_ID, people_id)
    if success:
        return jsonify({"message": "Favorite removed"}), 200
    return jsonify({"message": "Favorite not found"}), 404