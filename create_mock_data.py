
import base64
import os
from models import Basis, db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
import config
import uuid


def save_mock_data():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{config.db_user_name}:{config.db_user_password}@localhost/{config.db_name}'

    db.init_app(app)
    
    with app.app_context():  # Flask App-Kontext
        path = os.path.join(os.getcwd(), "mock_data")
        
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            with open(file_path, "rb") as f:
                encoded_string = base64.b64encode(f.read()).decode("utf-8")

            new_image = Basis(
                id=uuid.uuid4(),
                image_name=file, 
                image=encoded_string
            )
            db.session.add(new_image)  # db.session verwenden
            print(f" -> {file} hinzugefügt")

        db.session.commit()
        print("all pics saved in db")

if __name__ == "__main__":
    save_mock_data()