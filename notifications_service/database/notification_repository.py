from . import models, schema, exceptions
from sqlalchemy.orm import Session

class NotificationRepository():
    def register_device(self, device: schema.DeviceBase, db: Session):
        
        db_device = models.Device(
            user_id=device.user_id,
            token=device.token
        )
        db.add(db_device)
        db.commit()
        return db_device
    
    def get_device_token_from_user(self, userId: int, db: Session):
        user = db.query(models.Device).filter(models.Device.user_id == userId).first()
        if not user:
            raise exceptions.UserNotFoundError 
        return user.token

    