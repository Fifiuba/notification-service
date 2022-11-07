from pydantic import BaseModel

class DeviceToken(BaseModel):
    user_id: int
    device_id: str # TODO: chequear el type