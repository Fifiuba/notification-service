from pydantic import BaseModel

class DeviceBase(BaseModel):
    user_id: int
    token: str

    class Config:
        orm_mode = True

class NotificationRequest(BaseModel):
    user_id: int 
    title: str
    body: str 
    data: str
