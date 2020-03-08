import sqlite3
from sqlite3 import Error
from flask import Flask,render_template,request,session,url_for,redirect,flash
from os import urandom

from flask import g

from passlib.hash import sha256_crypt

import ssl
import urllib
import json
import random

import db_search as search
import db_updater as update
import db_builder as builder



app = Flask(__name__)
app.secret_key = urandom(32)

DATABASE = '/data/DAC.db'

@app.route("/",methods=['GET','POST'])
def home():
    builder.main()

    if 'username' in session: #if user is logged in
        print("YOU ARE LOGGED IN MICHELLE. ")
        return render_template("home2.html")
    else:
        print("YOU ARE NOT LOGGED IN MICHELLE. ")
        return render_template("login.html")

@app.route("/auth",methods=['GET','POST'])
def authPage():
    if 'username' in session:
        username = session['username']
        print("YOU ARE LOGGED IN MICHELLE. ")
        return redirect(url_for('home'))
    else:
        try:
            print("YOU ARE NOT LOGGED IN MICHELLE. wrong credentials ")

            username=request.form['username'] #username
            password = request.form['password'] #password that matches the username
            print("this is password " + password)
            if password == None: #if credentials are incorrect
                return redirect(url_for('home')) #redirects
            if (password == search.password(username)):
                print("got here i think?")
                session['username'] = username
                print("here")
                return redirect(url_for('home'))
            else: #else credentials are wrong
                print('Wrong Username or Password!')
                return redirect(url_for('home'))
        except:
            return redirect(url_for('home'))


@app.route("/auth2",methods=['GET','POST'])
def register():
    print("you are in register rn ")
    return render_template("auth2.html")

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route("/added",methods=['GET','POST'])
def added():
    try:
        if request.form['password'] == request.form['confirmpassword']:
            newUsername = request.form['email']
            newPassword = request.form['password']
            # userList = search.username(newUsername)
            print("below is userlist")
            # print(userList)
            # if userList == [] : #if username isn't taken
            update.addUser("",newUsername,newPassword) #add to database
            print('Register Successful')
            return redirect(url_for('home'))
            # else: #if username is taken
                # print('Username Taken')
                # return render_template("auth2.html")
        else:
            print("Passwords don't match")
            # return render_template("auth2.html")
    except:
        print("what happened")
        return render_template("auth2.html")


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
# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

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
    # db = get_db();
    app.run(debug = True)
