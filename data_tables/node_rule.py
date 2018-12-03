from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class NodeRule(Base):
    __tablename__ = 'node_rule'
    id = Column(Integer, primary_key=True)
    node = Column(Integer, ForeignKey("node.id"), nullable=False)
    rule = Column(Integer, ForeignKey("rule.id"), nullable=False)

    def __init__(self, node, rule):
        self.node = node
        self.rule = rule
     