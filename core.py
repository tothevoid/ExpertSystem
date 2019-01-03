from ui import UserInterface
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

class ESystem():
    def __init__(self):
        self.excersises = []
        self.root_id = 1
        self.user_id = 1
        self.db = Db(Base)

        self.ui = UserInterface(self.user_id, self.db.session)
        self.ui.init_user_input()
        self.get_exercises(self.root_id)

    def get_exercises(self,child_id):
        relations = self.db.session.query(Relation).filter_by(parent=child_id)
        if relations.count() == 0:
            return
        for rel in relations:
            rules = self.db.session.query(NodeRule).filter_by(node=rel.child)
            isPassed = True
            for rule in rules:
                if not self.evaulate_rule(rule):
                    isPassed = False
            if isPassed:
                exercise = self.db.session.query(Exercise).filter_by(node=rel.id)
                self.excersises.append(exercise)
                self.get_exercises(rel.child)

    def evaulate_rule(self,rule):
        rule_info = self.db.session.query(Rule).filter_by(id=rule.id)
        left_operand = self.db.session.query(UserData).filter_by(user = self.user_id, characteristic = rule_info.left_operand).value
        right_operand = rule_info.right_operand

        if rule_info.operator == '<' and int(left_operand) < int(right_operand):
            return True
        elif rule_info.operator == '>' and int(left_operand) > int(right_operand):
            return True
        elif rule_info.operator == '=' and int(left_operand) == int(right_operand):
            return True
        return False

    
      
    