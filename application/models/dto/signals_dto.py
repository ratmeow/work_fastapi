from uuid import UUID
from pydantic import BaseModel


class SignalsDTO(BaseModel):
    id = int
    object_uuid = UUID
    value = float
