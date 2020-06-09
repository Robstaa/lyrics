from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

SQLITE = 'sqlite'
ARTISTS = 'artists'
LYRICS = 'lyrics'


engine = create_engine('sqlite:///lyrics.db', echo=True)
Base = declarative_base()