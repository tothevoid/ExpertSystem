from data_tables.base import Base
from data_tables.db import Db

from data_tables.characteristic import Characteristic
from data_tables.muscle_group import MuscleGroup
from data_tables.node import Node
from data_tables.exercise import Exercise
from data_tables.node_rule import NodeRule
from data_tables.relation import Relation
from data_tables.rule import Rule
from data_tables.user_data import UserData
from data_tables.user import User

def fill_characteristics():
    db.session.add(Characteristic('Вес',10,60))
    db.session.commit()
    # print(self.session.query(Characteristic).filter_by(name='Вес').count())

db = Db(Base) 
db.create_tables()
fill_characteristics()