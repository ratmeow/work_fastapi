import uuid
from pydantic import BaseModel


class GridsDTO(BaseModel):
    uuid = uuid
    geometry_uuid = uuid
    object_uuid = uuid
    inline = int
    xline = int