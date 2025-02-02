from flask_sqlalchemy import SQLAlchemy

# Database initialization
db = SQLAlchemy()


# Declaration of database models
class Zones(db.Model):
    __tablename__ = 'zone'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    timezone = db.Column(db.String(20))
