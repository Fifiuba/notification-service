from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from notifications_service.database import database, models

session = None

# database
def init_database(app):
    engine = create_engine(
        "sqlite:///./test.db", echo=False, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[database.get_db] = override_get_db
    return TestingSessionLocal()