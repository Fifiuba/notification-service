from pydantic import BaseModel

class DeviceTokenBase(BaseModel):
    user_id: int
    device_id: str # TODO: chequear el type