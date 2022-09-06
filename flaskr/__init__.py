import os
import sqlite3

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

#https://flask.palletsprojects.com/en/2.1.x/config/#SECRET_KEY
#It’s set to 'dev' to provide a convenient value during development, but it should be overridden with a random value when deploying.

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return('Hello World !')
    
    from . import db
    """from . means relative import (in this repository); db means db.py"""
    db.init_app(app)

    return app