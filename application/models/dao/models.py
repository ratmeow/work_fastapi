from sqlalchemy import Column, ForeignKey, Boolean, Integer, Numeric, String, Text, DateTime, Float, Enum, JSON
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum
#Объявление декларативного (описательного) метода представления БД
Base = declarative_base()

# перечисление всех возможных типов объектов

Base = declarative_base()

class Object(Base):
    __tablename__ = 'objects'
    uuid = Column(UUID(as_uuid=True), primary_key=True)
    object_type = Column(String)
    props = Column(JSON)

    geometries = relationship('Geometry', back_populates='object')

class Geometry(Base):
    __tablename__ = 'geometries'
    id = Column(Integer, primary_key=True)
    geom = Column(Geometry('POINT', srid=4326))
    object_uuid = Column(UUID(as_uuid=True), ForeignKey('objects.uuid'))

    object = relationship('Object', back_populates='geometries')


#добавить поля





