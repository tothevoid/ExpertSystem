from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from base import Base

class Node(Base):
    __tablename__ = 'node'
    id = Column(Integer, primary_key=True)
    excercise = Column(Integer, ForeignKey("exercise.id"), nullable=True)
    
    def __init__(self, id, excercise = None):
        self.id = id
        if excercise != None:
            self.excercise = excercise