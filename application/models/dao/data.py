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


class Types(enum.Enum):
    d2seism = '2dseism'
    d3seism = '3dseism'
    grid = 'grid'
    map = 'map'
    horizon = 'horizon'
    whell = 'whell'
    whellbore = 'whellbore'
    inclinometry = 'inclinometry'
    gis = 'gis'
    marker = 'marker'
    signal = 'signal'
    library = 'library'


class Relation(enum.Enum):
    copy = 'copy'
    include = 'include'
    link = 'link'


class Objects(Base):
    __tablename__ = 'objects'
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    object_type = Column(Enum(Types), nullable=False)
    props = Column(JSON)
    source = Column(JSON)
    created_by = Column(UUID(as_uuid=True)) #ForeignKey('users.uuid', ondelete='CASCADE')
    project_uuid = Column(UUID(as_uuid=True)) #ForeignKey('projects.uuid', ondelete='CASCADE')
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class RelationObjects(Base):
    __tablename__ = 'relation_objects'
    parent_uuid = Column(UUID(as_uuid=True), ForeignKey('objects.uuid', ondelete='CASCADE'), primary_key=True)
    child_uuid = Column(UUID(as_uuid=True), ForeignKey('objects.uuid', ondelete='CASCADE'), primary_key=True)
    relation_type = Column(Enum(Relation))

class Geometries(Base):
    __tablename__ = 'geometries'
    uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    geom = Column(Geometry('POINT'))
    object_uuid = Column(UUID(as_uuid=True), ForeignKey('objects.uuid', ondelete='CASCADE'))
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
class Grids(Base):
    __tablename__ = 'grids'
    uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    geometry_uuid = Column(UUID(as_uuid=True), ForeignKey('geometries.uuid', ondelete='CASCADE'))
    object_uuid = Column(UUID(as_uuid=True), ForeignKey('objects.uuid', ondelete='CASCADE'))
    inline = Column(Integer)
    xline = Column(Integer)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class Surfaces(Base):
    __tablename__ = 'surfaces'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    grid_uuid = Column(UUID(as_uuid=True), ForeignKey('grids.uuid', ondelete='CASCADE'))
    object_uuid = Column(UUID(as_uuid=True), ForeignKey('objects.uuid', ondelete='CASCADE'))
    value = Column(Float)
    level = Column(Integer)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class WellData(Base):
    __tablename__ = 'well_data'
    uuid = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    geometry_uuid = Column(UUID(as_uuid=True), ForeignKey('geometries.uuid', ondelete='CASCADE'))
    object_uuid = Column(UUID(as_uuid=True), ForeignKey('objects.uuid', ondelete='CASCADE'))
    value = Column(Float)
    dm = Column(Float)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Markers(Base):
    __tablename__ = 'markers'
    id = Column(Integer, primary_key=True)
    well_data_uuid = Column(UUID(as_uuid=True), ForeignKey('well_data.uuid'), nullable=False)
    object_uuid = Column(UUID(as_uuid=True), ForeignKey('objects.uuid'), nullable=False)
    name = Column(String)
    dm = Column(Float)

class Signals(Base):
    __tablename__ = 'signals'
    id = Column(Integer, primary_key=True)
    object_uuid = Column(UUID(as_uuid=True), ForeignKey('objects.uuid'), nullable=False)
    value = Column(Float)







