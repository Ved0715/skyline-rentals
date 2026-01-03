import uuid
from datetime import datetime
from app import db


class Lease(db.Model):
    __tablename__ = 'leases'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    unit_id = db.Column(db.String(36), db.ForeignKey('units.id', ondelete='CASCADE'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    monthly_rent = db.Column(db.Numeric(10, 2), nullable=False)
    security_deposit = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')  # active, expired, terminated
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    payments = db.relationship('Payment', backref='lease', lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self, include_user=False, include_unit=False, include_payments=False):
        """Convert lease to dictionary."""
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'unit_id': self.unit_id,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'monthly_rent': float(self.monthly_rent) if self.monthly_rent else None,
            'security_deposit': float(self.security_deposit) if self.security_deposit else None,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        
        if include_user and self.user:
            data['user'] = self.user.to_dict()
        
        if include_unit and self.unit:
            data['unit'] = self.unit.to_dict()
        
        if include_payments:
            data['payments'] = [payment.to_dict() for payment in self.payments]
        
        return data

    def __repr__(self):
        return f'<Lease {self.id} - {self.status}>'
