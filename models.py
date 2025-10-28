
from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy import UUID

db = SQLAlchemy()


class Basis(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4)
    image = db.Column(db.Text)
    image_name = db.Column(db.String(100))