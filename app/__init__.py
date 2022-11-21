

#Import the flask class from the flask module
from flask import Flask
# Import SQLAlchemy and migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# IMPORT CONFIG FROM CONFIG
from config import Config

# Create instance of the Flask Class - central object of the whole app
app = Flask(__name__)

# Add a Secret_Key to the app config
#CONFIGURE THE APP USING THE CONFIG CLASS AND THE .FORM_OBJECT() METHOD
app.config.from_object(Config)

# Create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app)
# Ceate instance of Migrate to represent our migration engine
migrate = Migrate(app, db, render_as_batch=True)
# Create an instance of LoginManager to let our app allow login capabilities
login = LoginManager(app)

# import all of the routes and models from the routes and models module in the current folder
from . import routes, models
