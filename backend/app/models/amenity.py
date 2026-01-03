import uuid
from datetime import datetime
from app import db


class UnitAmenity(db.Model):
    __tablename__ = 'unit_amenities'

    unit_id = db.Column(db.String(36), db.ForeignKey('units.id', ondelete='CASCADE'), primary_key=True)
    amenity_id = db.Column(db.String(36), db.ForeignKey('amenities.id', ondelete='CASCADE'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Amenity(db.Model):
    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(100), nullable=True)  # Icon name or URL
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    units = db.relationship('Unit', secondary='unit_amenities', backref='amenities')

    def to_dict(self):
        """Convert amenity to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'icon': self.icon,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Amenity {self.name}>'
