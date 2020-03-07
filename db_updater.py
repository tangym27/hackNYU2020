# UncommonApp
# Dennis Chen, T Fabiha, Addison Huang, Michelle Tang
# P#02: The End
# ''' this file stores the updating database code'''

import sqlite3



def addUser(fullName, username, password):
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO usersAccounts (fullName, username, password, rating, longitude, latitude) VALUES(?,?,?,?,?,?)"
    params=(fullName, username,password,0,0,0)
    c.execute(insert,params)
    db.commit()
    db.close()

addUser("a","as","asf")

def addRestaurantAccounts(fullName, username, password, name, description, longitude, latitude ):
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO restaurantsAccounts (fullName , username , password , name , description , rating , longitude , latitude ) VALUES (?,?,?,?,?,?,?,?)"
    params=(fullName, username, password, name, description,0,longitude,latitude)
    c.execute(insert,params)
    db.commit()
    db.close()

addRestaurantAccounts("fullname","bob","s burger" ,"mcdonlads","as", 15.3,234.2)

def addMatches(id1, id2, id3, id4, restaurant):
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO matches(userAcc1,userAcc2,userAcc3,userAcc4,status, restaurant) VALUES(?,?,?,?,?,?)"
    params=(id1, id2, id3, id4, 0,restaurant )
    c.execute(insert,params)
    db.commit()
    db.close()


addMatches(1,2,0,0, "donalds")


def addDietRestrictions(userOrRestaurant, id, isVeg, isKos, isHal, isPes, isVegan):
    DB_FILE="./data/DAC.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO dietaryRestrictions (userOrRestaurant, accountID, vegetarian, kosher, halal, pescatarian, vegan) VALUES(?,?,?,?,?,?,?)"
    params=( userOrRestaurant, id, isVeg, isKos, isHal, isPes, isVegan )
    c.execute(insert,params)
    db.commit()
    db.close()

addDietRestrictions(1,1,0,0,0,0,0)
