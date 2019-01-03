from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from base import Base

class Relation(Base):
    __tablename__ = 'relation'
    id = Column(Integer, primary_key=True)
    parent = Column(Integer, ForeignKey("node.id"), nullable=False)
    child = Column(Integer, ForeignKey("node.id"), nullable=False)

    def __init__(self, parent, child):
        self.parent = parent
        self.child = child