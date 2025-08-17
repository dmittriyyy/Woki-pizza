from ..extensions import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False) 
    description = db.Column(db.String(200))

    pizzas = db.relationship("Pizza", back_populates="category")

    def __repr__(self):
        return f"<Category {self.name}>"