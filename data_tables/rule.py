from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Rule(Base):
    __tablename__ = 'rule'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    explanation = Column(String(400))
    left_operand = Column('user_id', Integer, ForeignKey("characteristic.id"), nullable=False)
    right_operand = Column(String(200))
    operator = Column(String(10))

    def __init__(self, name, explanation, left_operand, right_operand, operator):
        self.name = name
        self.explanation = explanation
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.operator = operator