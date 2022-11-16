from pydantic import BaseModel

class DeviceBase(BaseModel):
    user_id: int
    device_token: str

class NotificationRequest(BaseModel):
    user_id: int 
    title: str
    body: str 
    data: str
