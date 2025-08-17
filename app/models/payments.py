from ..extensions import db
from datetime import datetime

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    method = db.Column(db.String(20), nullable=False)   # card, cash, online
    status = db.Column(db.String(20), default="pending")  # pending, paid, failed
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    order = db.relationship("Order", back_populates="payment")

    def __repr__(self):
        return f"<Payment Order={self.order_id} Status={self.status}>"