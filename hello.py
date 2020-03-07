import sqlite3
from sqlite3 import Error
from flask import Flask
from flask import g

app = Flask(__name__)
DATABASE = '/data/DAC.db'

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/greet/<name>')
def greet(name):
    return 'Hello %s! How can I help you?' % name

@app.route('/decimals/<float:number>')
def decimal(number):
    return 'The URL you entered returned %f' % number

@app.route('/users/<int:id>')
def single_user():
    return get_users_by_ID(get_db())
# ________________________________
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_users(db):
    cur = db.cursor()
    cur.execute('SELECT * FROM usersAccounts')
    return cur.fetchall()

def get_users_by_ID(db, id):
    cur = db.cursor()
    cur.execute('SELECT * FROM userAccounts WHERE id = @id')
    return cur.fetchall();

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    db = get_db();
    app.run(debug = True)
