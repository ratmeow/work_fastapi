import enum

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