#Import the flask class from the flask module
from flask import Flask


# Create instance of the Flask Class - central object of the whole app
app = Flask(__name__)


# import all of the routes from the routes module in the current folder
from . import routes
