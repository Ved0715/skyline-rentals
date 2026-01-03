from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({"message": "Apartment Rental API", "status": "running"})

@bp.route('/health')
def health():
    return jsonify({"status": "healthy"})