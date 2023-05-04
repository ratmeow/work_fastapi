from application.services.repository import ObjectDAO
from application.models.dto.objects_dto import ObjectsDTO
from application.session import SessionLocal
#перед отправление в репозиторий превратить в DAO
class ObjectService:
    def __init__(self):
        with SessionLocal as session:
            self.dao = ObjectDAO(session)

    def create_object(self, obj: ObjectsDTO):
        obj = self.dao.create(obj.object_type, obj.created_by)
        return obj