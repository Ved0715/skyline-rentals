import uuid
from datetime import datetime
from app import db


class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    lease_id = db.Column(db.String(36), db.ForeignKey('leases.id', ondelete='CASCADE'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_date = db.Column(db.Date, nullable=True)
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # pending, completed, failed, overdue
    transaction_id = db.Column(db.String(100), nullable=True)
    payment_method = db.Column(db.String(50), nullable=True)  # card, bank_transfer, cash, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self, include_lease=False):
        """Convert payment to dictionary."""
        data = {
            'id': self.id,
            'lease_id': self.lease_id,
            'amount': float(self.amount) if self.amount else None,
            'payment_date': self.payment_date.isoformat() if self.payment_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'status': self.status,
            'transaction_id': self.transaction_id,
            'payment_method': self.payment_method,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        
        if include_lease and self.lease:
            data['lease'] = self.lease.to_dict()
        
        return data

    def __repr__(self):
        return f'<Payment {self.id} - {self.status}>'
