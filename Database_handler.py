from libdw import pyrebase
import datetime
import json 

from config import db
    
class OrderHandler():
    def __init__(self,database,store_name):
        # the class object take two parameters
        # the databse object and the name of the store 
        self.db= database
        self.store_name=store_name
        # the functions is to be used throughout the objects to parse datetime string 
        self.time_stamp= lambda: str(datetime.datetime.now()).split('.')[0]
    def update(self, status,order_number,*args):
        completed={}
        if status=='ready':
            # update the status and time of completion
            self.db.child('active_orders').child(self.store_name).child(order_number).update({"status":status})
            self.db.child('active_orders').child(self.store_name).child(order_number).update({"time_of_order_completion":self.time_stamp()}) 
        elif status=='cooking':
            #update the time of receving the orders
            self.db.child('active_orders').child(self.store_name).child(order_number).update({"status":status})
        elif status=='collected':
            # the function then will remove the orders from the active order to completed orders

            self.active=self.db.child('active_orders').child(self.store_name).child(order_number).get()

            self.complete=self.db.child('completed_orders').child(self.store_name).child(order_number)
            for entry in self.active.each():
                print(entry.key(),entry.val())
                if entry.key()=='status':
                    # change the status 
                    completed['status']='collected'
                elif entry.key()=='time_of_order_collection':
                    # update the time of completions 
                    completed['time_of_order_collection']=self.time_stamp()
                else:
                    completed[entry.key()]=entry.val()
                #set or update
            self.complete.update(completed) # To update the imformation 
            # then remove the order from active orders 
            self.active=self.db.child('active_orders').child(self.store_name).child(order_number).remove()
            return completed
        
    def get_all_order(self):
        self.orders={}
        stores=self.db.child('active_orders').child(self.store_name).get()
        for entry in stores.each():
            if entry.key()[0] !='!': # as some of the order to is to maintain the parental nodes 
                self.orders[entry.key()]= entry.val() # append all the neceesary details 
            #print((entry.val()))
        return self.orders # return the order details in dictionary 

#dbhandler= OrderHandler(db,'indian_stall')
#dbhandler.update('ready','100200604004')
#print(dbhandler.get_all_order())