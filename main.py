from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
import config

app = Flask(__name__)

# PostgreSQL-Verbindung
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql+psycopg2://{config.db_user_name}:{config.db_user_password}@localhost/{config.db_name}"
)


db.init_app(app)

with app.app_context():
    db.create_all()
    print("✅ Tabellen erfolgreich in der Datenbank erstellt.")