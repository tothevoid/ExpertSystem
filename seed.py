from base import Base
from db import Db

from characteristic import Characteristic
from muscle_group import MuscleGroup
from node import Node
from exercise import Exercise
from node_rule import NodeRule
from relation import Relation
from rule import Rule
from user_data import UserData
from user import User

def fill_characteristics():
    db.session.add(Characteristic('Вес',10,60))
    db.session.commit()
    
    # print(self.session.query(Characteristic).filter_by(name='Вес').count())

db = Db(Base) 
db.create_tables()
fill_characteristics()