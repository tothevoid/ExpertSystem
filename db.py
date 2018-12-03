#TODO: simplify
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from data_tables.characteristic import Characteristic
from data_tables.exercise import Exercise
from data_tables.muscle_group import MuscleGroup
from data_tables.node_rule import NodeRule
from data_tables.node import Node
from data_tables.relation import Relation
from data_tables.rule import Rule
from data_tables.user_data import UserData
from data_tables.user import User

from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine("mysql://root:Worldmw1337@localhost/esystem")

Base = declarative_base()
Base.metadata.create_all(engine)

# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
# user = Node("","","")
# session.add(user)
# session.commit()
# print(session.query(Node).filter_by(name='ivan').count())