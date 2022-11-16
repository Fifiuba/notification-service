from fastapi import APIRouter, status, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from typing import List, Union
from notifications_service.database import schema, database
from notifications_service.database.notification_repository import Notification_repository
from notifications_service.model.notificationManager import NotificationManager


#from users_service.utils import authorization_handler, token_handler, firebase_handler

notification_router = APIRouter()
notification_repository = Notification_repository()
notificationManager = NotificationManager()

@notification_router.post("/new_user", status_code=status.HTTP_201_CREATED)
async def register_device(device: schema.DeviceBase, db: Session = Depends(database.get_db)):
        return notification_repository.register_device(device,db)


@notification_router.post("/", status_code=status.HTTP_201_CREATED)
async def notify_user(req: Request, db: Session = Depends(database.get_db)):
        try:
               #user_id = json.loads(req.body)['passengerId']
               #device_token = notification_repository.get_device_token_from_user(user_id, db)
               #req.body
               #device_token = 
               notificationManager.send_push_notification(device_token, "Prueba de notificacion")
               return result
        except (exceptions.UserInfoException) as error:
               raise HTTPException(**error.__dict__)