from flask import render_template
from app import app

# Create a route for our app
@app.route('/')
def index():
    user_info = {
        'username': 'Apocalipsis',
        "email": "Apocalip@gmail.com"
        }
    colors = ["red","blue","Silver",'Black','Burgandy','Cyan',]
    return render_template('index.html', user=user_info, colors=colors)
    


@app.route('/posts')
def posts():
    return 'Hi this is Posts'
