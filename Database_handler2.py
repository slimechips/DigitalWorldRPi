from libdw import pyrebase
import datetime
import json 
url = "https://digitalworldf08g2.firebaseio.com/"
apikey = "AIzaSyDHyug6TDWAda_ZirZ1G7B9cFV525ahvyk"

config = {
    "apiKey": apikey,
    "databaseURL": url,
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

x=db.child('active_orders').child('western_stall').child('order_000001').get()

    
class DatabaseHandler():
    def __init__(self,database,store_name):
        self.db= database
        self.store=store_name
        self.time_stamp= lambda: str(datetime.datetime.now()).split('.')[0]
    def update(self, status,order_number):
        completed={}
        if status=='ready':
            self.db.child('active_orders').child(self.store).child(order_number).update({"status":status})
            self.db.child('active_orders').child(self.store).child(order_number).update({"time_of_order_completion":self.time_stamp()}) 

        elif status=='completed':
            self.active=self.db.child('active_orders').child('western_stall').child(order_number).get()
            self.complete=self.db.child('completed_orders').child('western_stall').child(order_number)
            for entry  in self.active.each():
                print(entry.key(),entry.val())
                if entry.key()=='status':
                    completed['status']='collected'
                elif entry.key()=='time_of_order_collection':
                    completed['time_of_order_collection']=self.time_stamp()
                else:
                    completed[entry.key()]=entry.val()
            self.complete.set(completed)
            self.active=self.db.child('active_orders').child(self.store).child(order_number).remove()
            return completed

dbhandler= DatabaseHandler(db,'western_stall')
data= dbhandler.update("completed",'order_000004')

def order(db,data):
    data['time_of_order_collection']='None'
    data['time_of_order_completion']='None'
    data['food_item']="Rice without chicket"
    data['status']= 'received'
    print(data)
    db.child('active_orders').child('western_stall').child('order_000004').set(data)

