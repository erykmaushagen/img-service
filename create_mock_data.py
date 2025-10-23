
import base64
import os
from models import Basis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config


def save_mock_data():
    path ="/mock_data"
    index = 0

    for file in os.listdir(path): 

        encoded_string = base64.b64encode(file.read()).decode("utf-8")
        new_image = Basis(id = index, image_name = file, image = encoded_string)


        # active db: 
        engine = create_engine(f'postgresql+psycopg2://{config.db_user_name}:{config.db_user_password}@localhost/{config.db_name}')
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(new_image)
        session.commit()

if __name__ == "__main__": 

    save_mock_data()