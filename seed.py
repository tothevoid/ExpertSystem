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
    """Бесполезный метод ;-;"""
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
    """Заполнение таблицы характеристик"""
    filepath = 'data\\fill_characteristics.txt'
    with open(filepath, "r", encoding="ansi") as dataf:
        data = dataf.readlines()
        for line in data:
            line = line.replace('\n','')
            values = line.split('\t')
            #print(values)
            db.session.add(Characteristic(values[0],float(values[1]),float(values[2])))
        db.session.commit()  
    print("Import characteristics success!")

def fill_muscle_group():
    """Заполнение таблицы групп мышц"""
    filepath = 'data\\fill_muscle_group.txt'
    with open(filepath, "r", encoding="ansi") as dataf:
        data = dataf.readlines()
        for line in data:
            line = line.replace('\n','')
            values = line.split('\t')
            #print(values)
            db.session.add(MuscleGroup(values[0]))
        db.session.commit()  
    print("Import muscle group success!")

def fill_exercise():
    """Заполнение упражнений и узлов дерева"""
    filepath = 'data\\fill_exercise.txt'
    with open(filepath, "r", encoding="ansi") as dataf:
        data = dataf.readlines()
        nodeIdList = []
        for line in data:
            line = line.replace('\n','')
            values = line.split('\t')
            nodeIdList.append(int(values[0]))
            #print(values)
            exercise = Exercise(values[1],values[2],int(values[3]))
            db.session.add(exercise)            
        db.session.commit()  
        
        exerciseId = 1
        for nodeId in nodeIdList:
            node = Node(nodeId,int(exerciseId))
            db.session.add(node)
            exerciseId += 1           
        db.session.commit()  
    print("Import exercise and node success!")
    
def fill_rulse():
    """Заполнение правил и привязки правил к узлам"""
    filepath = 'data\\fill_rules.txt'
    with open(filepath, "r", encoding="ansi") as dataf:
        data = dataf.readlines()     
        nodeIdList = []
        for line in data:
            line = line.replace('\n','')
            values = line.split('\t')
            #print(values)
            nodeIdList.append(int(values[0]))
            rule = Rule(values[1],int(values[2]),values[3],values[4])
            db.session.add(rule)
        db.session.commit()  

        idRule = 1
        for nodeId in nodeIdList:
            node_rule = NodeRule(nodeId,idRule)
            db.session.add(node_rule)
            idRule+=1          
        db.session.commit()
    print("Import rule and node rule success!")

def update_tables():
    db.drop_tables()
    db.create_tables()

def fill_db():
    fill_characteristics()
    fill_muscle_group()
    fill_exercise()
    fill_rulse()

db = Db(Base)
update_tables()
fill_db()