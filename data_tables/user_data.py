from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class UserData(Base):
    __tablename__ = 'user_data'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    characteristic = Column(Integer, ForeignKey("characteristic.id"), nullable=False)

    def __init__(self, user, characteristic):
        self.user = user
        self.characteristic = characteristic
     