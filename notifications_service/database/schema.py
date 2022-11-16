from pydantic import BaseModel

class DeviceBase(BaseModel):
    user_id: int
    device_token: str