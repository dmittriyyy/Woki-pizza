from ..extensions import db
from datetime import datetime

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    price = db.Column(db.Numeric(10, 2), nullable=False)  # фиксируем цену на момент заказа

    order = db.relationship("Order", back_populates="items")
    pizza = db.relationship("Pizza", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem Order={self.order_id} Pizza={self.pizza_id} x{self.quantity}>"