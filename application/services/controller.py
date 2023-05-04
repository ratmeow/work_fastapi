from application.services.service import ObjectService

class ObjectController:
    def __init__(self):
        service = ObjectService()
        self.service = service

    def create_object(self, obj: ObjectsDTO):
        result = self.service.create_object(obj)
        return result

#