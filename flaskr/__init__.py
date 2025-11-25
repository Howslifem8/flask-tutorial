#importing sys os module & Flask 
import os 
from flask import Flask

#This file holds the 'Application Factory' function create_app()

def create_app(test_config=None):
    #create and configure the app 

    #create Flask instance
    app = Flask(__name__, instance_relative_config=True)

    #sets default config that the app will use 
        #secret key used to protect data, must be changed when deploying to production
        #Using os module to path the database file
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None: 
        #load the instance config, if it exists, when not testing 
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Load the test config is passed in 
        app.config.from_mapping(test_config)
    
    # ensure instance folder exists 

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #a simple route that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db
    db.init_app(app)
    
    return app



