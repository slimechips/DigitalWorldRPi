from libdw import pyrebase

apikey = "AIzaSyDHyug6TDWAda_ZirZ1G7B9cFV525ahvyk"
authDomain = "digitalworldf08g2.firebaseapp.com"
databaseURL = "https://digitalworldf08g2.firebaseio.com/"

config = {
    "apiKey": apikey,
    "databaseURL": databaseURL,
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
