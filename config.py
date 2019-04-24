from libdw import pyrebase
# Contains the config for my firebase
# This file is standalone since it contains my API key and is added to the gitignore
# P.s. prof please don't steal my api key :)
apikey = "AIzaSyDHyug6TDWAda_ZirZ1G7B9cFV525ahvyk"
authDomain = "digitalworldf08g2.firebaseapp.com"
databaseURL = "https://digitalworldf08g2.firebaseio.com/"

config = {
    "apiKey": apikey,
    "databaseURL": databaseURL,
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
