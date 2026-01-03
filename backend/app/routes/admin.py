from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.amenity import Amenity
from app.models.lease import Lease
from app.models.payment import Payment
from app.models.user import User
from app.utils.decorators import admin_required

bp = Blueprint('admin', __name__)

# --- Amenities Management ---

@bp.route('/amenities', methods=['GET'])
def get_amenities():
    """Get all amenities (Public)."""
    amenities = Amenity.query.filter_by(is_active=True).all()
    return jsonify([a.to_dict() for a in amenities]), 200

@bp.route('/amenities', methods=['POST'])
@jwt_required()
@admin_required()
def create_amenity():
    """Admin creates a new amenity."""
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'message': 'Name is required'}), 400

    amenity = Amenity(
        name=data['name'],
        description=data.get('description'),
        icon=data.get('icon')
    )
    
    try:
        db.session.add(amenity)
        db.session.commit()
        return jsonify(amenity.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

# --- Tenant & Lease Management ---

@bp.route('/leases', methods=['GET'])
@jwt_required()
@admin_required()
def get_leases():
    """Admin views all active leases (Tenants)."""
    leases = Lease.query.all()
    return jsonify([l.to_dict(include_user=True, include_unit=True) for l in leases]), 200

# --- Payments (Mock Data) ---

@bp.route('/payments', methods=['GET'])
@jwt_required()
@admin_required()
def get_payments():
    """Admin views all payments."""
    payments = Payment.query.all()
    return jsonify([p.to_dict(include_lease=True) for p in payments]), 200

@bp.route('/dashboard/stats', methods=['GET'])
@jwt_required()
@admin_required()
def get_dashboard_stats():
    """Admin dashboard statistics."""
    # Simple counts
    total_users = User.query.count()
    active_leases = Lease.query.filter_by(status='active').count()
    pending_payments = Payment.query.filter_by(status='pending').count()
    
    return jsonify({
        'total_users': total_users,
        'active_tenants': active_leases,
        'pending_payments': pending_payments
    }), 200
