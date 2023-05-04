from application.models.dao.models import *
from application.session import SessionLocal
import traceback
import functools

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

    @dbexception
    def create(self, object_type, props):
        uuid_val = str(uuid.uuid4())
        obj = Object(uuid=uuid_val, object_type=object_type, props=props)
        # self.db.add(obj)
        # self.db.commit()
        # self.db.refresh(obj)
        return obj

