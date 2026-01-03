import uuid
from datetime import datetime
from app import db


class Tower(db.Model):
    __tablename__ = 'towers'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    total_floors = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    units = db.relationship('Unit', backref='tower', lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self):
        """Convert tower to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'total_floors': self.total_floors,
            'description': self.description,
            'unit_count': self.units.count(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Tower {self.name}>'
