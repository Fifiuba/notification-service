from pydantic import BaseModel

class DeviceBase(BaseModel):
    user_id: int
    device_id: str # TODO: chequear el type