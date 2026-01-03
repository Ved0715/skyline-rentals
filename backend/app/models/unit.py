import uuid
from datetime import datetime
from app import db


class Unit(db.Model):
    __tablename__ = 'units'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tower_id = db.Column(db.String(36), db.ForeignKey('towers.id', ondelete='CASCADE'), nullable=False)
    unit_number = db.Column(db.String(20), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    area_sqft = db.Column(db.Numeric(10, 2), nullable=False)
    monthly_rent = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='available')  # available, occupied, maintenance
    description = db.Column(db.Text, nullable=True)
    images = db.Column(db.JSON, nullable=True, default=list)  # Array of image URLs
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    bookings = db.relationship('Booking', backref='unit', lazy='dynamic', cascade='all, delete-orphan')
    leases = db.relationship('Lease', backref='unit', lazy='dynamic', cascade='all, delete-orphan')

    # Unique constraint: unit_number must be unique within a tower
    __table_args__ = (
        db.UniqueConstraint('tower_id', 'unit_number', name='unique_unit_in_tower'),
    )

    def to_dict(self, include_tower=False, include_amenities=False):
        """Convert unit to dictionary."""
        data = {
            'id': self.id,
            'tower_id': self.tower_id,
            'unit_number': self.unit_number,
            'floor': self.floor,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'area_sqft': float(self.area_sqft) if self.area_sqft else None,
            'monthly_rent': float(self.monthly_rent) if self.monthly_rent else None,
            'status': self.status,
            'description': self.description,
            'images': self.images or [],
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        
        if include_tower and self.tower:
            data['tower'] = self.tower.to_dict()
        
        if include_amenities:
            data['amenities'] = [amenity.to_dict() for amenity in self.amenities]
        
        return data

    def __repr__(self):
        return f'<Unit {self.unit_number}>'
