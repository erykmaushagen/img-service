
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Basis(db.Model):
    id = db.Column(db.String(20), primary_key = True, nullable=False)
    image = db.Column(db.Text)
    image_name = db.Column(db.String(100))