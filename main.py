from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<int:username>')
def hello_user(username):
    return 'Hello, User #%d!' % username
