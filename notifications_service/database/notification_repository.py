from . import models, schema
from sqlalchemy.orm import Session

class Notification_repository():
    def register_device(self, device: schema.DeviceBase, db: Session):
        
        db_device = models.Device(
            user_id=device.user_id,
            device_id=device.device_id
        )
        db.add(db_device)
        db.commit()
        #db.refresh(deb_device)
        return db_device
    
    def get_device_tokens_from_user(self, userId: int, db: Session):
        #pasar a un crud
        return db.query(models.Device).filter(models.Device.user_id == userId)

    def send_push_notification(self,notification_parameters: dict, userId: int, db: Session):
        tokens = self.get_device_tokens_from_user(user_id, db)
        #TODO: investigar que devuelve el batch response
        batch_response = fmc.sendPush(
                device_tokens=tokens,
                data=notification_parameters.get('data'),
                title=notification_parameters.get('title'),
                body=notification_parameters.get('body')
            )