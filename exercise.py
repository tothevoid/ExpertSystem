from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from base import Base

class Exercise(Base):
    __tablename__ = 'exercise'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    description = Column(String(200))
    muscle_group = Column(Integer, ForeignKey("muscle_group.id"), nullable=False)

    def __init__(self, name, min_value, max_value):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value