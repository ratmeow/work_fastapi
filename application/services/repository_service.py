from typing import Optional, Iterable
from sqlalchemy.orm import Session
import functools
import traceback

from application.models.dao.data import *


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

@dbexception
def add_data(db: Session) -> bool:
    obj1 = Objects(
        uuid=uuid.uuid4(),
        object_type=Types.d2seism,
        props={'prop1': 10, 'prop2': 'test'},
        source={'source1': 1, 'source2': 'test'},
        created_by=uuid.uuid4(),
        project_uuid=uuid.uuid4()
    )
    db.add(obj1)

    obj2 = Objects(
        uuid=uuid.uuid4(),
        object_type=Types.gis,
        props={'prop3': 20, 'prop4': 'test2'},
        source={'source3': 2, 'source4': 'test2'},
        created_by=uuid.uuid4(),
        project_uuid=uuid.uuid4()
    )
    db.add(obj2)

    db.commit()

    # добавление связи между объектами
    rel_obj1_obj2 = RelationObjects(
        parent_uuid=obj1.uuid,
        child_uuid=obj2.uuid,
        relation_type=Relation.link
    )
    db.add(rel_obj1_obj2)

    # добавление геометрий
    geom1 = Geometries(
        uuid=uuid.uuid4(),
        geom='POINT(1 2)',
        object_uuid=obj1.uuid
    )
    db.add(geom1)

    geom2 = Geometries(
        uuid=uuid.uuid4(),
        geom='POINT(3 4)',
        object_uuid=obj2.uuid
    )
    db.add(geom2)

    # добавление сеток
    grid1 = Grids(
        uuid=uuid.uuid4(),
        geometry_uuid=geom1.uuid,
        object_uuid=obj1.uuid,
        inline=1,
        xline=2
    )
    db.add(grid1)

    grid2 = Grids(
        uuid=uuid.uuid4(),
        geometry_uuid=geom2.uuid,
        object_uuid=obj2.uuid,
        inline=3,
        xline=4
    )
    db.add(grid2)

    # добавление поверхностей
    surf1 = Surfaces(
        grid_uuid=grid1.uuid,
        object_uuid=obj1.uuid,
        value=10.0,
        level=1
    )
    db.add(surf1)

    surf2 = Surfaces(
        grid_uuid=grid2.uuid,
        object_uuid=obj2.uuid,
        value=20.0,
        level=2
    )
    db.add(surf2)

    # добавление данных скважин
    well_data1 = WellData(
        uuid=uuid.uuid4(),
        geometry_uuid=geom1.uuid,
        object_uuid=obj1.uuid,
        value=30.0,
        dm=1.0
    )
    db.add(well_data1)

    well_data2 = WellData(
        uuid=uuid.uuid4(),
        geometry_uuid=geom2.uuid,
        object_uuid=obj2.uuid,
        value=40.0,
        dm=1.0
    )
    db.add(well_data2)

    db.commit()

    marker1 = Markers(well_data_uuid=well_data1.uuid, object_uuid=obj1.uuid, name='marker_1', dm=100.0)
    marker2 = Markers(well_data_uuid=well_data2.uuid, object_uuid=obj2.uuid, name='marker_2', dm=200.0)
    db.add_all([marker1, marker2])

    # создаем записи в таблице signals
    signal1 = Signals(object_uuid=obj1.uuid, value=1.0)
    signal2 = Signals(object_uuid=obj2.uuid, value=2.0)
    db.add_all([signal1, signal2])
    return True

