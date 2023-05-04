from application.models.dao.models import *
#переписать с декоратором, вместо класса функции
def dbexception(db_func):
    @functools.wraps(db_func)
    def decorated_func(db: Session, *args, **kwargs) -> bool:
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
    def __init__(self, db: Session):
        self.db = db
#генерировать uuid
    def create(self, uuid, object_type, props):
        obj = Object(uuid=uuid, object_type=object_type, props=props)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

