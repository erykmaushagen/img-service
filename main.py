from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
import config

app = Flask(__name__) # neue Flask-Anwendung

# Datenbankverbindung konfigurieren
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql+psycopg2://{config.db_user_name}:{config.db_user_password}@localhost/{config.db_name}"
)


db.init_app(app) # db in flask integrieren, verwendet dabei 

with app.app_context(): # tabellen erstellen
    db.create_all()
    print("✅ Tabellen erfolgreich in der Datenbank erstellt.")