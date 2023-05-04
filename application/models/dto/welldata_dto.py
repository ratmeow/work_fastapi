from uuid import UUID
from pydantic import BaseModel


class WellDataDTO(BaseModel):
    uuid: UUID
    geometry_uuid: UUID
    object_uuid: UUID
    value: float
    dm: float
