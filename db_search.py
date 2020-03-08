import sqlite3 #imports sqlite

###############
# useraccount #
###############
def username(username):
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    user_exists = 'SELECT username FROM usersAccounts WHERE usersAccounts.username = (?);'
    c.execute(user_exists,(username,))
    userList = c.fetchall()
    return userList # empty list if person isnt there otherwise okay.

def password(username):
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    get_password = 'SELECT password FROM usersAccounts WHERE usersAccounts.username = (?)'
    c.execute(get_password,(username,))
    password = c.fetchone()
    return password[0] # returns the password for a given username


def getAllRestaurants():
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT name FROM restaurantsAccounts;"
    c.execute(command)
    tList = c.fetchall()
    fList = []
    for element in tList:
        fList.append(str(element[0]))
    db.commit()
    db.close()
    return(fList)

print(getAllRestaurants()) #lists of all the restaurants

def getID(username):
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT id FROM usersAccounts WHERE usersAccounts.username ='" + username + "';" #selects score of the user
    c.execute(command)
    id = c.fetchone()[0]
    db.commit()
    db.close()
    return(id)

def getUsersDietRestriction(username):
    id = str(getID(username))
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM dietaryRestrictions WHERE dietaryRestrictions.id ='" + id + "';"
    c.execute(command)
    restrictions = c.fetchall()

    db.commit()
    db.close()
    return(restrictions[0])

def getUserLocation(username):
    id = str(getID(username))
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT longitude,latitude FROM usersAccounts WHERE usersAccounts.username ='" + username + "';"
    c.execute(command)
    location = c.fetchall()

    db.commit()
    db.close()
    return(location[0])

def getRestaurantLocation(username):
    id = str(getID(username))
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT longitude,latitude FROM restaurantsAccounts WHERE restaurantsAccounts.username ='" + username + "';"
    c.execute(command)
    location = c.fetchall()
    db.commit()
    db.close()
    return(location[0])

# def updateRatings(username, rating):
#     DB_FILE="./data/DAC.db"
#     db = sqlite3.connect(DB_FILE)
#     c = db.cursor()
#     command = "SELECT longitude,latitude FROM restaurantsAccounts WHERE restaurantsAccounts.username ='" + username + "';"
#     c.execute(command)
#     location = c.fetchall()
#     db.commit()
#     db.close()
