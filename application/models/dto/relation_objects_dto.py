import uuid
from pydantic import BaseModel


class RelationObjectsDTO(BaseModel):
    parent_uuid: uuid
    child_uuid: uuid
    ralation_type: relation