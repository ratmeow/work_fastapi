import uuid
import json

from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime


class ObjectsDTO(BaseModel):
    """ DTO для добавления, обновления и получения информации о погоде.
        Если данные, передаваемые клиенту сильно отличаются от данных,
        которые принимает REST API сервера, необходимо разделять DTO
        для запросов и ответов """
    # uuid: uuid
    created_by: uuid
    project_uuid: uuid
    object_type: types
    props: json
    source: json


