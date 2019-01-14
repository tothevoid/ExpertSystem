from flask import Flask, request, send_from_directory, render_template, url_for, abort
import graph_builder
import json

from base import Base
from db import Db
from characteristic import Characteristic
from user_data import UserData
from user import User
from node import Node
from characteristic import Characteristic
from muscle_group import MuscleGroup
from exercise import Exercise

import core

app = Flask(__name__,static_url_path='')
app.config.update(
   TEMPLATES_AUTO_RELOAD = True,
   SEND_FILE_MAX_AGE_DEFAULT = 0
)

db = Db(Base)
user_id = 1

@app.route("/")
def start_page():
   res = []
   for characteristic in db.session.query(Characteristic).all():
      if characteristic.name == "Тип тренировки":
         continue
      res.append(characteristic.__dict__)
   return render_template('user_input.html', characteristics = res)
  
@app.route("/tree")
def show_tree():
   return render_template('tree.html')

@app.route("/get_graph")
def get_graph():
   edges, nodes = graph_builder.get_graph(False)
   out_edges = []
   for item in edges:
      values = dict()
      start = dict()
      start['id'] = item.start.id
      end = dict()
      end['id'] = item.end.id
      values['start'] = start
      values['end'] = end
      out_edges.append(values)
   node_json = [ob.__dict__ for ob in nodes]
   out = dict()
   out['nodes'] = node_json
   out['edges'] = out_edges
   return json.dumps(out)

@app.route("/get_user_form", methods=['POST'])
def get_user_form():
   if not request.json:
      abort(400)
   # users = db.session.query(User).all()
   user_data = db.session.query(UserData).filter_by(user = 1).one_or_none()
   if user_data == None:
      for key,value in request.json.items():
         char_id = key.split('_')
         if len(char_id) != 2:
            continue
         else:
            char_id = char_id[1]
         db.session.add(UserData(user_id, char_id, value))
      db.session.commit()
   return 'success'

@app.route("/add_node", methods=['POST'])
def add_node():
    abort(400)
    return 'success' 

@app.route("/get_excercies")
def get_excercies():
   output = core.ESystem()
   res = output.excersises

@app.route("/get_data")
def get_data():
    def create_dict(dic):
        for ob in dic:
            ob.pop('_sa_instance_state', None)
        return dic
        ob.pop('_sa_instance_state', None)

    nodes = db.session.query(Node)
    characteristics = db.session.query(Characteristic)
    muscle_groups = db.session.query(MuscleGroup)
    exercises = db.session.query(Exercise)
    node_json = create_dict([ob.__dict__ for ob in nodes])
    characteristics_json = create_dict([ob.__dict__ for ob in characteristics])
    muscle_groups_json = create_dict([ob.__dict__ for ob in muscle_groups])
    exercises_json = create_dict([ob.__dict__ for ob in exercises])
    out = dict()
    out['nodes'] = node_json
    out['characteristics'] = characteristics_json
    out['muscle_groups'] = muscle_groups_json
    out['exercises'] = exercises_json
    return json.dumps(out)


if __name__ == "__main__":
   app.run()