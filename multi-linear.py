from libdw import pyrebase
import numpy as np
import datetime

import os
url= "https://digitalworldf08gg2.firebaseio.com/"
apikey = "AIzaSyDHyug6TDWAda_ZirZ1G7B9cFV525ahvyk"

config= {
    "apiKey": apikey,
    "databaseURL":url
    }

firebase= pyrebase.initialize_app(config)
db=firebase.database()
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
class pred_time():
    def __init__(self,db,store):
        self.time_cal=lambda time1: datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S') 
        self.store= store
        self.db= db
        self.regressor= LinearRegression()
        time_data,queue= self.get_data()
        self.regressor.fit(time_data,queue)
    def time_difference(self,time1, time2):
        time1= time_cal(time1)
        time2= time_cal(time2)
        time_difference= abs(time1-time2)
        return time_difference
    def get_data(self):
        time_data=[]
        queue=[]
        entries=self.db.child("completed_orders").child(self.store).get()
        for item in entries.each():
            info=item.val() 
            time1=info['time_of_order']
            time2= info['time_of_order_completion']
            time_diff= self.time_difference(time1,time2)
            time_data.append([time_difference])
            queue.append([info['orders_in_queue']]) 
        return time_data, queue
    def pred (self,orders):
        orders=[]
        stores=self.db.child('active_orders').child(self.store).get()
        for entry in stores.each():
            orders.append(entry.key())
        #.reshape(t_time.shape[0],-1)
        pred_time=self.regressor.pred([[len(orders)-1]])
        self.db.child('active_orders').child(self.store).child(orders).set(pred_time)
        return pred_time
