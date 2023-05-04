from uuid import UUID
from pydantic import BaseModel


class MarkersDTO(BaseModel):
    id = int
    well_data_uuid = UUID
    object_uuid = UUID
    name = str
    dm = float
