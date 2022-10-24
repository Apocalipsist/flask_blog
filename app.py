#Import the flask class from the flask module
from flask import Flask
# Create instance of the Flask Class - central object of the whole app
app = Flask(__name__)


# Create a route for our app
@app.route('/')
def index():
    return 'hello this is the index route'

@app.route('/posts')
def posts():
    return 'Hi this is Posts'
