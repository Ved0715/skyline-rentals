from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.booking import Booking
from app.models.unit import Unit
from app.utils.decorators import admin_required

bp = Blueprint('bookings', __name__)

#create booking
@bp.route('/', methods=['POST'])
@jwt_required()
def create_booking():
    data = request.get_json()
    user_id = get_jwt_identity()
    
    if not data or not data.get('unit_id'):
        return jsonify({'message': 'Unit ID is required'}), 400
        
    unit = db.session.get(Unit, data['unit_id'])
    if not unit:
        return jsonify({'message': 'Unit not found'}), 404
        
    booking = Booking(
        user_id=user_id,
        unit_id=data['unit_id'],
        preferred_move_in=data.get('preferred_move_in'),
        user_notes=data.get('user_notes')
    )
    
    try:
        db.session.add(booking)
        db.session.commit()
        return jsonify({'message': 'Booking requested successfully', 'booking': booking.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error creating booking', 'error': str(e)}), 500

#Get bookings
@bp.route('/my', methods=['GET'])
@jwt_required()
def get_my_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return jsonify([b.to_dict(include_unit=True) for b in bookings]), 200

#admin
#git all bookings
@bp.route('/', methods=['GET'])
@jwt_required()
@admin_required()
def get_all_bookings():
    bookings = Booking.query.all()
    return jsonify([b.to_dict(include_user=True, include_unit=True) for b in bookings]), 200

#Update bookings status
@bp.route('/<booking_id>/status', methods=['PUT'])
@jwt_required()
@admin_required()
def update_booking_status(booking_id):
    data = request.get_json()
    status = data.get('status')
    
    if status not in ['approved', 'declined', 'cancelled']:
        return jsonify({'message': 'Invalid status'}), 400
        
    booking = db.session.get(Booking, booking_id)
    if not booking:
        return jsonify({'message': 'Booking not found'}), 404
        
    booking.status = status
    booking.admin_notes = data.get('admin_notes', booking.admin_notes)
    
    try:
        db.session.commit()
        return jsonify({'message': f'Booking {status}', 'booking': booking.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error updating booking', 'error': str(e)}), 500