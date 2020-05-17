from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/name')
def welcome():
    return "Welcome to our application!"

@app.route('/welcome/<person>')
def welcome_home(person):
    return f"Dear {person}, Welcome Home!!!"

@app.route('/welcome/<int:number>')
def number_add(number):
    return f"I guess your favorite number is {number}. \
                It is half of {number * 2}"
