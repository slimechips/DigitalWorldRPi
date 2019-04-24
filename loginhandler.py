from config import config
from libdw import pyrebase

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def check_credentials(username, password):
    # Check user credentials
    user_valid = check_username(username)
    if user_valid:
        pw_valid = check_password(username, password)
    return user_valid, pw_valid

def check_username(username):
    # Checks if username exists
    db_username = db.child("stall_users").child(username)
    if db_username != None:
        return True
    else:
        return False

def check_password(username, password):
    # Checks if password entered is correct
    db_pw = db.child("stall_users").child(username).child("password")
    if password == db_pw:
        return True
    else:
        return False

