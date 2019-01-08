from flask import Flask, request, send_from_directory, render_template, url_for, abort
import json
app = Flask(__name__,static_url_path='')
app.config.update(
   TEMPLATES_AUTO_RELOAD = True,
   SEND_FILE_MAX_AGE_DEFAULT = 0
)

@app.route("/")
def start_page():
   return render_template('user_input.html')
   # return send_from_directory('static', 'index.html')
  
def send_nodes():
   pass

@app.route("/tree")
def show_tree():
   return render_template('tree.html')

@app.route("/get_user_form", methods=['POST'])
def get_user_form():
   if not request.json:
      abort(400)
   print(request.json)
   return json.dumps(request.json)

@app.route("/show_excercises")
def show_excercises():
   pass

if __name__ == "__main__":
   app.run()