from ..extensions import db

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image_url = db.Column(db.String(200))
    is_available = db.Column(db.Boolean, default=True)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", back_populates="pizzas")

    order_items = db.relationship("OrderItem", back_populates="pizza")

    def __repr__(self):
        return f"<Pizza {self.name} - {self.price}>"