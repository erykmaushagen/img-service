
import base64
import os
from models import Basis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config


def save_mock_data():
    path = os.path.join(os.getcwd(), "mock_data")  # relativer Pfad
    engine = create_engine(
        f'postgresql+psycopg2://{config.db_user_name}:{config.db_user_password}@localhost/{config.db_name}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for index, file in enumerate(os.listdir(path)):
        file_path = os.path.join(path, file)
        with open(file_path, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode("utf-8")

        new_image = Basis(id=str(index), image_name=file, image=encoded_string)
        session.add(new_image)

    session.commit()
    session.close()
    print("all pics saved in db")

if __name__ == "__main__":
    save_mock_data()