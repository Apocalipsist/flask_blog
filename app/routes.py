from flask import render_template
from app import app
from app.forms import SignUpForm

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
    return render_template('posts.html')

@app.route('/signup')
def signup():
    forms = SignUpForm()
    return render_template('signup.html', form=forms)
