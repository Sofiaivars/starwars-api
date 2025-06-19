from flask import Blueprint, jsonify
from services.user_service import get_all_users

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify(users), 200