from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from base import Base

class Rule(Base):
    __tablename__ = 'rule'
    id = Column(Integer, primary_key=True)
    explanation = Column(String(400))
    left_operand = Column(Integer, ForeignKey("characteristic.id"), nullable=False)
    right_operand = Column(String(200))
    operator = Column(String(10))

    def __init__(self, explanation, left_operand, right_operand, operator):
        self.explanation = explanation
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.operator = operator