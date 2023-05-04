from uuid import UUID
from pydantic import BaseModel


class GridsDTO(BaseModel):
    uuid = UUID
    geometry_uuid = UUID
    object_uuid = UUID
    inline = int
    xline = int
