from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from base import Base

class Characteristic(Base):
    __tablename__ = 'characteristic'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    min_value = Column(Integer)
    max_value = Column(Integer)

    def __init__(self, name, min_value, max_value):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value