import uuid
from pydantic import BaseModel


class WellDataDTO(BaseModel):
    uuid: uuid
    geometry_uuid: uuid
    object_uuid: uuid
    value: float
    dm: float