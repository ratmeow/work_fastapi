import uuid
from pydantic import BaseModel


class MarkersDTO(BaseModel):
    id = int
    well_data_uuid = uuid
    object_uuid = uuid
    name = str
    dm = float