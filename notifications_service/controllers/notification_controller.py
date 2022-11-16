from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Union
from notifications_service.database import schema, database,exceptions
from notifications_service.database.notification_repository import NotificationRepository
from notifications_service.model.notification_manager import NotificationManager


#from users_service.utils import authorization_handler, token_handler, firebase_handler

notification_router = APIRouter()
notification_repository = NotificationRepository()
notificationManager = NotificationManager()

@notification_router.post("/new_user",response_model=schema.DeviceBase,status_code=status.HTTP_201_CREATED)
async def register_device(device: schema.DeviceBase, db: Session = Depends(database.get_db)):
        return notification_repository.register_device(device,db)



@notification_router.post("/", status_code=status.HTTP_200_OK)
async def notify_user(notification: schema.NotificationRequest, db: Session = Depends(database.get_db)):
        try:
                user_id = notification.user_id
                token = notification_repository.get_device_token_from_user(userId, db)
                # cambiar el parametro a notification entero
                res = notificationManager.send_push_notification(device_token, notification.title,notification.body)
                return res.status 
        except (exceptions.NotificationException) as error:
               raise HTTPException(**error.__dict__)
        except (exceptions.UserNotFoundError) as error:
               raise HTTPException(**error.__dict__)