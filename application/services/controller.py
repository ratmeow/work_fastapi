from application.services.service import *

class ObjectController:
    def __init__(self, service):
        self.service = service

    def create_object(self):
        data = request.get_json()
        obj = self.service.create_object(data['uuid'], data['object_type'], data['props'])
        obj_dto = ObjectDTO.from_object(obj)
        return jsonify(obj_dto.to_dict())

#