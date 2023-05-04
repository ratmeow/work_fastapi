from application.models.dao.models import *
from application.models.dao.dao import *

class ObjectRepository:
    def __init__(self, dao: ObjectDAO):
        self.dao = dao

    def create(self, uuid, object_type, props):
        obj = self.dao.create(uuid, object_type, props)
        return obj
