from uuid import UUID
from pydantic import BaseModel


class SurfacesDTO(BaseModel):
    id = int
    grid_uuid = UUID
    object_uuid = UUID
    value = float
    level = int
