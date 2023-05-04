from uuid import UUID
from geoalchemy2 import Geometry
from pydantic import BaseModel


class GeometriesDTO(BaseModel):
    uuid = UUID
    geom = Geometry
    object_uuid = UUID
