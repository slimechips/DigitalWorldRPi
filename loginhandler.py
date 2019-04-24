from config import db

# Stores current stall user
cur_stall_user = None

# Stores current stall stall id
cur_stall_id = None

def check_credentials(username, password):
    # Check user credentials
    user_valid = check_username(username)
    pw_valid = None
    if user_valid:
        pw_valid = check_password(username, password)
    return user_valid, pw_valid

def check_username(username):
    # Checks if username exists
    db_username = db.child("stall_users").child(username).get().val()
    print("useraname", db_username)
    if db_username != None:
        return True
    else:
        return False

def check_password(username, password):
    # Checks if password entered is correct
    db_pw = db.child("stall_users").child(username).child("password").get().val()
    print("pw", db_pw)
    if password == db_pw:
        # If password is correct, return the stall_id of the stall
        return db.child("stall_users").child(username).child("stall_id").get().val()
    else:
        return None

