from application.session import SessionLocal
from application.services.repository_service import *
import random
from application.models.dao.data import *

""" Данный скрипт заполняет БД тестовыми данными """

def test(session):
    add_data(session)
    # добавление тестовых объектов


if __name__ == "__main__":
    with SessionLocal() as session:
        test(session)
