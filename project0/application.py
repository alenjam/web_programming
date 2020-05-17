from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"

@app.route('/sub/<int:number1>/<int:number2>')
def sub(number1, number2):
    return f"{number1} - {number2} = {number1 - number2}"

@app.route('/mul/<int:number1>/<int:number2>')
def mul(number1, number2):
    return f"{number1} * {number2} = {number1 * number2}"

@app.route('/div/<int:number1>/<int:number2>')
def div(number1, number2):
    return f"{number1} / {number2} = {number1 / number2}"
