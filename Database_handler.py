from libdw import pyrebase
import datetime
import json 



    
class OrderHandler():
    def __init__(self,database,store_name): # the object takes in database handler, and name of the store
        self.db= database
        self.store=store_name
        #this mini function is to for the class method to get the current time in string
        self.time_stamp= lambda: str(datetime.datetime.now()).split('.')[0]
    def update(self, status,order_number):
        completed={} # The take the order from active order to completed orders
        if status=='ready': 
            #with order ready, it mean it is ready to be collectted  
            self.db.child('active_orders').child(self.store).child(order_number).update({"status":status})
            self.db.child('active_orders').child(self.store).child(order_number).update({"time_of_order_completion":self.time_stamp()}) 
        elif status=='cooking':
            # when the order is received by the vendor, 
            self.db.child('active_orders').child(self.store).child(order_number).update({"status":status})
           
        elif status=='collected':
            # this is to remove the orders from the active order and put it into 
            # active oder
            self.active=self.db.child('active_orders').child('western_stall').child(order_number).get()
            self.complete=self.db.child('completed_orders').child('western_stall').child(order_number)
            for entry  in self.active.each():
                #extracted the order detail from active order
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
            self.orders[entry.key()]= entry.val()
            print(type(entry.val()))
        return self.orders

dbhandler= OrderHandler(db,'western_stall')
dbhandler.update('collected','234300604001')