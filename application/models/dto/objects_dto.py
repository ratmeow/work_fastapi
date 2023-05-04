from uuid import UUID
from enum_classes import Types
from pydantic import BaseModel



class ObjectsDTO(BaseModel):
    """ DTO для добавления, обновления и получения информации о погоде.
        Если данные, передаваемые клиенту сильно отличаются от данных,
        которые принимает REST API сервера, необходимо разделять DTO
        для запросов и ответов """
    # uuid: UUID
    created_by: UUID
    project_uuid: UUID
    object_type: Types
    props: dict
    source: dict


