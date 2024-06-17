from sqlmodel import SQLModel, create_engine, Session
from models.doctor import Doctor
from models.video import Video

scheme="postgresql"
host="127.0.0.1"
port=5432
user="root"
password="postgres"
db_name="medoh-db"

POSTGRES_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(POSTGRES_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

if __name__ == "__main__":  
    create_db_and_tables()