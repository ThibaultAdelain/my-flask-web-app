from flask import Flask
from flask import render_template
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
@app.route('/<name>')
@app.route('/index.html/<name>')
def index(name=None):
    return render_template("index.html", name=name)

@app.route('/user/<name>/')
def helloName(name):
    return(f'Welcome user {name} !')

# n'accepte que les int

@app.route('/user/<int:id>/')
def helloId(id):
    return(f'Welcome user number {id} !')

@app.route('/path/<path:subpath>/')
def showSubPath(subpath):
    return(f'Subpath: {subpath}')

@app.route('/hello/')
def hello():
    return('Hello World !')

# from markupsafe import escape

# @app.route('/<name>')
# def helloName(name):
#     return(f'hello {escape(name)} !')

