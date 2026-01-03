from flask import Blueprint, request, jsonify
from app import db
from flask_jwt_extended import jwt_required
from app.model.tower import Tower
from app.models.unit import Unit
from app.utils.decorators import admin_required

bp = Blueprint('units', __name__)
# view units
@dp.route('/units', method=['GET'])
def get_units():
    status = request.args.get('status')
    query = Units.query

    if status:
        query = query.filter_by(status=status)

    units = query.all()
    return jsonify([unit.to_dict(include_tower=True) for unit in units]), 200

#view unit details
@bp.route('/units/<unit_id>', methods=['GET'])
def get_unit(unit_id):
    unit = db.session.get(Unit, unit_id)
    if not unit:
        return jsonify({'message': 'Unit not found'}), 404
        
    return jsonify(unit.to_dict(include_tower=True, include_amenities=True)), 200

#view towers
@bp.route('/towers', methods=['GET'])
def get_towers():
    towers = Tower.query.all()
    return jsonify([tower.to_dict() for tower in towers]), 200


# admin
# create tower
@bp.route('/towers', methods=['POST'])
@jwt_required()
@admin_required()
def create_tower():
    data = request.get_json()
    
    if not data or not data.get('name') or not data.get('address') or not data.get('total_floors'):
        return jsonify({'message': 'Missing required fields'}), 400
        
    tower = Tower(
        name=data['name'],
        address=data['address'],
        total_floors=data['total_floors'],
        description=data.get('description')
    )
    
    try:
        db.session.add(tower)
        db.session.commit()
        return jsonify({'message': 'Tower created', 'tower': tower.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error creating tower', 'error': str(e)}), 500

#create unit
@bp.route('/units', methods=['POST'])
@jwt_required()
@admin_required()
def create_unit():
    data = request.get_json()
    
    required = ['tower_id', 'unit_number', 'floor', 'bedrooms', 'bathrooms', 'area_sqft', 'monthly_rent']
    if not data or not all(k in data for k in required):
        return jsonify({'message': 'Missing required fields'}), 400
        
    unit = Unit(
        tower_id=data['tower_id'],
        unit_number=data['unit_number'],
        floor=data['floor'],
        bedrooms=data['bedrooms'],
        bathrooms=data['bathrooms'],
        area_sqft=data['area_sqft'],
        monthly_rent=data['monthly_rent'],
        description=data.get('description'),
        status='available'
    )
    
    try:
        db.session.add(unit)
        db.session.commit()
        return jsonify({'message': 'Unit created', 'unit': unit.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error creating unit', 'error': str(e)}), 500
