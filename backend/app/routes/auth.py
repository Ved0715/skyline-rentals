from flask import Blueprint, request, jsonify

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # TODO: Implement registration
    return jsonify({"message": "Registration endpoint"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # TODO: Implement login
    return jsonify({"message": "Login endpoint"})