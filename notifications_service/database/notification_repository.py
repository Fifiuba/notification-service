from . import models, schema, exceptions
from sqlalchemy.orm import Session

class NotificationRepository():
    def register_device(self, device: schema.DeviceBase, db: Session):
        db_device =  db.query(models.Device).filter(models.Device.user_id == device.user_id).first()
        if not db_device:    
            db_device = self.create(device, db)
        else:
            self.update(db_device, device.token, db)
        return db_device
    
    def get_device_token_from_user(self, userId: int, db: Session):
        user = db.query(models.Device).filter(models.Device.user_id == userId).first()
        if not user:
            raise exceptions.UserNotFoundError 
        return user.token
    
    def get_all(self,db):
        devices = db.query(models.Device).all()
        return devices


    def update(self,db_device,token,db):
        setattr(db_device, "token", token)
        db.commit()
        db.refresh(db_device)

    def create(self,device,db):
        db_device = models.Device(
            user_id=device.user_id,
            token=device.token)
        db.add(db_device)
        db.commit()
        return db_device

    