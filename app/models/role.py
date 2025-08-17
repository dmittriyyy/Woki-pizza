from ..extensions import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200))

    users = db.relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role {self.name}>"