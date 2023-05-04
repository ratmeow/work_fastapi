from application.services.repository import *
from application.session import SessionLocal
#перед отправление в репозиторий превратить в DAO
class ObjectService:
    def __init__(self, repo: ObjectRepository):
        self.repo = repo

    def create_object(self, uuid, object_type, props):
        with SessionLocal as session:
            obj = self.repo.create(uuid, object_type, props)
        return obj