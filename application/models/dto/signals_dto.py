import uuid
from pydantic import BaseModel


class SignalsDTO(BaseModel):
    id = int
    object_uuid = uuid
    value = float