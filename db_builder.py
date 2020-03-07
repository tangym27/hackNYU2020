
import sqlite3 #imports sqlite


def usersAccounts(): #creates the users db
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    # db.execute("PRAGMA foreign_keys = 1")

    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE usersAccounts(id INTEGER PRIMARY KEY, fullName TEXT, username TEXT, password TEXT, rating REAL)"
    c.execute(command)

'''


'''
def restaurantsAccounts(): #creates the puzzles db
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    # db.execute("PRAGMA foreign_keys = 1")

    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE restaurantsAccounts(id INTEGER PRIMARY KEY, fullName TEXT, username TEXT, password TEXT, rating REAL)"
    c.execute(command)

'''


'''
def restaurants(): #creates the logs db
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    # db.execute("PRAGMA foreign_keys = 1")

    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE restaurants(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, address TEXT, description TEXXT, rating REAL)"
    c.execute(command)

def matches():
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    # db.execute("PRAGMA foreign_keys = 1")

    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE matches(id INTEGER PRIMARY KEY AUTOINCREMENT,\
     userAcc1 INTEGER, userAcc2 INTEGER, userAcc3 INTEGER, userAcc4 INTEGER, status INTEGER, restaurant TEXT,\
     FOREIGN KEY (userAcc1) REFERENCES usersAccounts(id))"
    c.execute(command)


def main(): #calls all of the functions to build the databases
    try:
        print("hm")
        usersAccounts()
        restaurantsAccounts()
        restaurants()
        matches()
        print("what")
    except:
        print("didnt work")
        pass

main()
print("databases created")
