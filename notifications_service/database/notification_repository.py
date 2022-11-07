from . import models, schema
from sqlalchemy.orm import Session

class Notification_repository():
    def register_device(device: schema.Device, db: Session):
        
        deb_device = models.Device(
            user_id=device.user_id
            device_id=device.device_id
        )
        db.add(deb_device)
        db.commit()
        #db.refresh(deb_device)
        return deb_device