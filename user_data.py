from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from base import Base

class UserData(Base):
    __tablename__ = 'user_data'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    characteristic = Column(Integer, ForeignKey("characteristic.id"), nullable=False)
    value = Column(Integer)

    def __init__(self, user, characteristic, value):
        self.user = user
        self.value = value
        self.characteristic = characteristic
     