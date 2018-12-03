from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Node(Base):
    __tablename__ = 'node'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    excercise = Column(Integer, ForeignKey("exercise.id"), nullable=False)
    
    def __init__(self, name, excercise):
        self.name = name
        self.excercise = excercise