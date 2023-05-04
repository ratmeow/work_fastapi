from uuid import UUID
from pydantic import BaseModel
from enum_classes import Relation


class RelationObjectsDTO(BaseModel):
    parent_uuid: UUID
    child_uuid: UUID
    relation_type: Relation
