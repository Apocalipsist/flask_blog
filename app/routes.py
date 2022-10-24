from app import app

# Create a route for our app
@app.route('/')
def index():
    return 'hello this is the index route'

@app.route('/posts')
def posts():
    return 'Hi this is Posts'
