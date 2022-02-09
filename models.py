from sqlalchemy import Column, Integer, String, ForeignKey,Float,create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:postgres@db/postgres')

Base = declarative_base()

class Cities(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lat = Column(Float)
    lon = Column(Float)
Base.metadata.create_all(engine)
