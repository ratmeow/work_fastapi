import uuid
from pydantic import BaseModel


class GeometriesDTO(BaseModel):
    uuid = uuid
    geom = geometry
    object_uuid = uuid