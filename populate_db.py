from application.session import SessionLocal
from application.services.repository_service import *
import random


""" Данный скрипт заполняет БД тестовыми данными """


CITY = ['UFA', 'MOSCOW', 'SAINT-PETERSBURG', 'NORILSK', 'KHERSON', 'CRIMEA']

TRANS_TYPE = [1, 2, 3, 4, 5, 6]


def populate_city(db: Session) -> None:
    for city_name in CITY:
        add_city(db, city_name)


def populate_trans_type(db: Session) -> None:
    for trans_type_name in TRANS_TYPE:
        add_type(db, trans_type_name)


if __name__ == "__main__":
    with SessionLocal() as session:
        populate_trans_type(session)
