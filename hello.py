import sqlite3
from flask import Flask
from flask import g

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/greet/<name>')
def greet(name):
    return 'Hello %s! How can I help you?' % name

@app.route('/decimals/<float:number>')
def decimal(number):
    return 'The URL you entered returned %f' % number

app.run(debug=True)
