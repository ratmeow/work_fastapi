from sqlalchemy import Column, ForeignKey, Boolean, Integer, Numeric, String, Text, DateTime, Float, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship
from datetime import datetime



#Объявление декларативного (описательного) метода представления БД
Base = declarative_base()
#ахах


class Type(enum.Enum):
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


class Object(Base):
    __tablename__ = 'objects'

    uuid = Column(String, primary_key=True)
    created_by = Column(String, ForeignKey('users.uuid'))
    project_uuid = Column(String, ForeignKey('projects.uuid'))
    object_type = Column(Enum(Type))
    props = Column(JSON)
    source = Column(JSON)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    geometries = relationship("Geometries", back_populates="object")
    grids = relationship("Grids", back_populates="object")
    surfaces = relationship("Surfaces", back_populates="object")
    well_data = relationship("WellData", back_populates="object")
    markers = relationship("Markers", back_populates="object")
    signals = relationship("Signals", back_populates="object")


class RelationObjects(Base):
    tablename = 'RelationObjects'

    parent_uuid = Column(ForeignKey('Objects.uuid'))
    child_uuid = Column(ForeignKey('Objects.uuid'))
    relation_type = Column(Enum(Relation.Enum))

class Geometries(Base):
    tablename = 'Geometries'

    id = Column(Integer, primary_key=True)
    geom = Column('geometry', String)
    object_uuid = Column(ForeignKey('Objects.uuid'), index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Grids(Base):
    tablename = 'Grids'

    id = Column(Integer, primary_key=True)
    geometry_id = Column(ForeignKey('Geometries.id'))
    object_uuid = Column(ForeignKey('Objects.uuid'))
    inline = Column(Integer)
    xline = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Surfaces(Base):
    tablename = 'Surfaces'

    id = Column(Integer, primary_key=True)
    grid_id = Column(ForeignKey('Grids.id'))
    object_uuid = Column(ForeignKey('Objects.uuid'))
    value = Column(Float)
    level = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class WellData(Base):
    tablename = 'WellData'

    id = Column(Integer, primary_key=True)
    geometry_id = Column(ForeignKey('Geometries.id'))
    object_uuid = Column(ForeignKey('Objects.uuid'))
    value = Column(Float)
    dm = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Markers(Base):
    tablename = 'Markers'

    id = Column(Integer, primary_key=True)
    well_data_id = Column(ForeignKey('WellData.id'))
    object_uuid = Column(ForeignKey('Objects.uuid'))
    name = Column(String)
    dm = Column(Float)


class Signals(Base):
    tablename = 'Signals'

    id = Column(Integer, primary_key=True)
    object_uuid = Column(ForeignKey('Objects.uuid'))
    value = Column(Float)










class Transformator(Base):
    """ Таблица с наименованиями населённых пунктов """
    __tablename__ = "transformator"

    id = Column(Integer, primary_key=True)
    number = Column('number', Integer, nullable=False)
    hydrogen = Column('hydrogen', Integer, nullable=False)
    oxygen = Column('oxygen', Integer, nullable=False)
    nitrogen = Column('nitrogen', Integer, nullable=False)
    methane = Column('methane', Integer, nullable=False)
    co = Column('co', Integer, nullable=False)
    co_2 = Column('co2', Integer, nullable=False)
    ethylene = Column('ethylene', Integer, nullable=False)
    ethane = Column('ethane', Integer, nullable=False)
    acethylene = Column('acethylene', Integer, nullable=False)
    dbds = Column('dbds', Integer, nullable=False)
    power_factor = Column('power_factor', Float, nullable=False)
    interfacial_v = Column('interfacial_v', Integer, nullable=False)
    dielectric_rigidity = Column('dielectric_rigidity', Integer, nullable=False)
    water_content = Column('water_content', Integer, nullable=False)
    health_index = Column('health_index', Float)

    city = Column(Integer, ForeignKey('city.id'), nullable=False)
    city_name = relationship('City')

    types = Column(Integer, ForeignKey('types.id'), nullable=False)
    transformator_type = relationship('Types')

    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    @hybrid_property
    def _health_index(self):
        """ Декоратор @hybrid_property позволяет добавить какую-нибудь бизнес-логику или проверку
            при установке данному полю какого-либо значения. Подробнее см.:
            https://docs.sqlalchemy.org/en/14/orm/extensions/hybrid.html#sqlalchemy.ext.hybrid.hybrid_property """
        return self.health_index

    @_health_index.setter
    def _health_index(self):
        """ При установке значения полю temperature_c будет автоматически рассчитано значение temperature_f """
        self.health_index = 100.0

    def update_health_index(self):
        pass

    def __repr__(self):
        """ Переопределяем строковое представление объекта (см. python magic methods)"""
        return f'{self.__dict__}'


class City(Base):
    """ Таблица с наименованиями населённых пунктов """
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    tmp = Column(uuid)

    def __repr__(self):
        """ Переопределяем строковое представление объекта (см. python magic methods)"""
        return f'{self.__dict__}'


class Types(Base):
    """ Таблица с наименованиями населённых пунктов """
    __tablename__ = "types"

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False, unique=True)

    def __repr__(self):
        """ Переопределяем строковое представление объекта (см. python magic methods)"""
        return f'{self.__dict__}'






