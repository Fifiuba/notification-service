from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from users_service.database.models import Base
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

def init_database():
    engine = create_engine(
        "postgresql://" + POSTGRES_USER + ":" + POSTGRES_PASSWORD + "@postgres:5432/device_tokens", echo=True
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