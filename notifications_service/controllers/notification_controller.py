from fastapi import APIRouter, status, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from typing import List, Union
from notifications_service.database import schema, database, notification_repository

#from users_service.utils import authorization_handler, token_handler, firebase_handler

notification_router = APIRouter()
notification_repository = Notification_repository()

@notification_router.post("", status_code=status.HTTP_201_CREATED)
async def register_device(device: schema.Device, db: Session = Depends(database.get_db)):
        return notification_repository.register_device(device,db)


@notification_router.post("/{id/]", status_code=status.HTTP_201_CREATED):
async def notify_driver(user_id: int, req: Request, db: Session = Depends(database.get_db)):
        result = notification_repository.send_push_notification(json.loads(req.body),user_id, db)
        #TODO: que pasa si no hay devices? devuelve error o como lo manejamos?
        #tambien que pasa si no hay un usuario registrado.
        return result