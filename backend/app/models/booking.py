import uuid
from datetime import datetime
from app import db


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    unit_id = db.Column(db.String(36), db.ForeignKey('units.id', ondelete='CASCADE'), nullable=False)
    requested_date = db.Column(db.DateTime, default=datetime.utcnow)
    preferred_move_in = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='pending')  # pending, approved, declined, cancelled
    admin_notes = db.Column(db.Text, nullable=True)
    user_notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self, include_user=False, include_unit=False):
        """Convert booking to dictionary."""
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'unit_id': self.unit_id,
            'requested_date': self.requested_date.isoformat() if self.requested_date else None,
            'preferred_move_in': self.preferred_move_in.isoformat() if self.preferred_move_in else None,
            'status': self.status,
            'admin_notes': self.admin_notes,
            'user_notes': self.user_notes,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        
        if include_user and self.user:
            data['user'] = self.user.to_dict()
        
        if include_unit and self.unit:
            data['unit'] = self.unit.to_dict()
        
        return data

    def __repr__(self):
        return f'<Booking {self.id} - {self.status}>'
