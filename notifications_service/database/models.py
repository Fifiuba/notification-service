from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeviceToken(Base):
    __tablename__ = "device_tokens"

    token = Column("token", String, nullable=False, primary_key=True)
    user_id = Column("user_id", Integer, nullable=False)
    
