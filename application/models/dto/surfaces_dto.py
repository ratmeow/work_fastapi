import uuid
from pydantic import BaseModel


class SurfacesDTO(BaseModel):
    id = int
    grid_uuid = uuid
    object_uuid = uuid
    value = float
    level = int