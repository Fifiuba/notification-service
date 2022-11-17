from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from notifications_service.database.models import Base
from dotenv import load_dotenv
import os

load_dotenv()

def init_database():
    postgresUser = str(os.environ.get('POSTGRES_USER'))
    postgresPassword = str(os.environ.get('POSTGRES_PASSWORD'))
    engine = create_engine(
        "postgresql://postgres:alejo@localhost:5432/postgres", echo=True
    )
    print("postgresql://" + postgresUser + ":" + postgresPassword + "@postgres:5432/")


    global SessionLocal
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)


def get_local_session():
    return SessionLocal()


# Dependency
def get_db():
    db = SessionLocal()
    print(db)
    try:
        yield db
    finally:
        db.close()