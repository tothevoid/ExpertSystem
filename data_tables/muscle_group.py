from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class MuscleGroup(Base):
    __tablename__ = 'muscle_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    
    def __init__(self, name):
        self.name = name
    # def __repr__(self):
    #     return "<MuscleGroup('%s','%s', '%s')>" % (self.name, self.fullname, self.password)