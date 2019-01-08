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
import re

def import_data(table, filepath):
    with open(filepath, "r", encoding="utf-8") as dataf:
        data = dataf.readlines()
        for line in data:
            line = line.replace('\n','')
            values = line.split(';')
            convertValues = []
            for val in values:
                res = re.match(r'\D',val)
                if res == None:
                    convertValues.append(float(val))
                else:
                    convertValues.append(val)
            #print(convertValues)
            db.session.add(table(*convertValues))
        db.session.commit()

def fill_characteristics():
    """Нужно указать путь к csv файлу"""
    filepath = 'data\\fill_characteristics.csv'
    import_data(Characteristic,filepath)    
    print("Import characteristics success!")
    # print(self.session.query(Characteristic).filter_by(name='Вес').count())

db = Db(Base)
db.create_tables()
fill_characteristics()