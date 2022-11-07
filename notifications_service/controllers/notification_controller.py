from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Union
from notifications_service.database import schema, database, notification_repository
#from users_service.utils import authorization_handler, token_handler, firebase_handler

notification_router = APIRouter()
notification_repository = Notification_repository()

@notification_router.post("", status_code=status.HTTP_201_CREATED)
async def register_device(device: schema.Device, db: Session = Depends(database.get_db)):
        return notification_repository.register_device(device,db)
