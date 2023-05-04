from application.models.dao.models import Objects
from application.session import SessionLocal
import traceback
import functools
import uuid

# переписать с декоратором, вместо класса функции
def dbexception(db_func):
    @functools.wraps(db_func)
    def decorated_func(db: SessionLocal, *args, **kwargs) -> bool:
        try:
            db_func(db, *args, **kwargs)    # вызов основной ("оборачиваемой") функции
            db.commit()     # подтверждение изменений в БД
            return True
        except Exception as ex:
            # выводим исключение и "откатываем" изменения
            print(f'Exception in {db_func.__name__}: {traceback.format_exc()}')
            db.rollback()
            return False
    return decorated_func


class ObjectDAO:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create(self, object_type, props, source, created_by, proj_uuid):
        uuid_val = uuid.uuid4()
        obj = Objects(uuid=uuid_val, object_type=object_type, props=props, source=source, created_by=created_by, project_uuid=proj_uuid)
        try:
            self.db.add(obj)
            self.db.commit()
            return True
        except Exception as ex:
            # выводим исключение и "откатываем" изменения
            print(f'Exception in {db_func.__name__}: {traceback.format_exc()}')
            self.db.rollback()
            return False

