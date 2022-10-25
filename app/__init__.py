# Installation Link
# https://flask.palletsprojects.com/en/2.2.x/installation/

# Quickstart Link
# https://flask.palletsprojects.com/en/2.2.x/quickstart/

# Jinja Template 
# https://jinja.palletsprojects.com/en/3.1.x/templates/

# Install or upgrade using pip.
# pip install -U Flask-WTF


#Import the flask class from the flask module
from flask import Flask



# Create instance of the Flask Class - central object of the whole app
app = Flask(__name__)
# Add a Secret_Key to the app config
app.config['SECRET_KEY'] = 'You-dont-know-nothing'

# import all of the routes from the routes module in the current folder
from . import routes
