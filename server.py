from flask import Flask, request, send_from_directory, render_template, url_for

app = Flask(__name__,static_url_path='')
app.config.update(
   TEMPLATES_AUTO_RELOAD = True,
   SEND_FILE_MAX_AGE_DEFAULT = 0
)

@app.route("/")
def start_page():
   # return send_from_directory('static', 'index.html')
   return render_template('index.html')

def send_nodes():
   pass

def show_user_form():
   pass

def get_user_form():
   pass

def show_excercises():
   pass

if __name__ == "__main__":
   app.run()
   url_for('static', filename='style.css')
   url_for('static', filename='graph.css')