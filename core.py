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

class ESystem():
    def __init__(self):
        self.excersises = []
        self.root_id = 1
        self.user_id = 1
        self.db = Db(Base)
        self.get_excercises(self.root_id)

    def get_excercises(self,child_id):
        relations = self.db.session.query(Relation).filter_by(parent=child_id)
        if relations.count() == 0:
            return
        for rel in relations:
            rules = self.db.session.query(NodeRule).filter_by(node=rel.child)
            isPassed = True
            isSaved = False
            for rule in rules:
                eval_res = self.evaulate_rule(rule.rule)
                if eval_res == False or eval_res == None:
                    isPassed = False
                if eval_res == None:
                    isSaved == True
            if isPassed:
                nodes = self.db.session.query(Node).filter_by(id=rel.child)
                for node in nodes:
                    excercise = self.db.session.query(Exercise).filter_by(id=node.excercise).one_or_none()
                    if excercise != None:
                        self.excersises.append(excercise)
            if isPassed and isSaved: 
                self.get_excercises(rel.child)

    def evaulate_rule(self,rule_id):
        rule_info = self.db.session.query(Rule).filter_by(id=rule_id).one_or_none()
        if rule_info == None:
            return None
        left_operand = self.db.session.query(UserData).filter_by(user = self.user_id, characteristic = rule_info.left_operand).one_or_none()
        if left_operand == None:
            return None
        right_operand = rule_info.right_operand

        if rule_info.operator == '<' and int(left_operand.value) < int(right_operand):
            return True
        elif rule_info.operator == '>' and int(left_operand.value) > int(right_operand):
            return True
        elif rule_info.operator == '=' and int(left_operand.value) == int(right_operand):
            return True
        return False