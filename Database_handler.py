from libdw import pyrebase
import datetime
import json 


    
class OrderHandler():
    def __init__(self,database,store_name):
        self.db= database
        self.store=store_name
        self.time_stamp= lambda: str(datetime.datetime.now()).split('.')[0]
    def update(self, status,order_number):
        completed={}
        if status=='ready':
            self.db.child('active_orders').child(self.store).child(order_number).set({"status":status})
            self.db.child('active_orders').child(self.store).child(order_number).set({"time_of_order_completion":self.time_stamp()}) 
        elif status=='cooking':
            self.db.child('active_orders').child(self.store).child(order_number).update({"status":status})
        elif status=='collected':
            self.active=self.db.child('active_orders').child(self.store_name).child(order_number).get()
            self.complete=self.db.child('completed_orders').child(self.store_name).child(order_number)
            for entry in self.active.each():
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
    def get_all_order(self):
        self.orders={}
        stores=self.db.child('active_orders').child(self.store).get()
        for entry in stores.each():
            if entry.key()[0] !='!':
                self.orders[entry.key()]= entry.val()
            print(type(entry.val()))
        return self.orders

dbhandler= OrderHandler(db,'japanese_stall')
#dbhandler.update('collected','234300604001')
print(dbhandler.get_all_order())