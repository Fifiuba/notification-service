from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from notifications_service.database.models import Base
from dotenv import load_dotenv
import os

load_dotenv()

def init_database():
    engine = create_engine(
        "postgresql://postgres:postgres@postgres:5432/postgres", echo=True
    )

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