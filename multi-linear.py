from libdw import pyrebase
import numpy as np
import datetime

import os
url = "https://digitalworldf08g2.firebaseio.com/"
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
        time1= self.time_cal(time1)
        time2= self.time_cal(time2)
        time_difference= abs(time1-time2)
        time_difference= abs(time_difference.total_seconds())/60
        return time_difference
    def get_data(self):
        time_data=[]
        queue=[]
        entries=self.db.child("completed_orders").child(self.store).get()
        for item in entries.each():
            info=item.val() 
            time1=info['time_of_order']
            time2= info['time_of_order_completion']
            print(time1, time2)
            time_diff= self.time_difference(time1,time2)
            time_data.append([time_diff])
            queue.append([info['orders_in_queue']]) 
        return time_data, queue
    def pred (self,orders):
        order_active=[]
        stores=self.db.child('active_orders').child(self.store).get()
        for entry in stores.each():
            order_active.append(entry.key())
        #.reshape(t_time.shape[0],-1)
        pred_time=self.regressor.predict([[len(order_active)-1]])
        self.db.child('active_orders').child(self.store).child(orders).child('estimated_waiting_time').set(pred_time[0,0])
        print('pred_time')
        return pred_time
pred=pred_time(db,'western_stall')
pred.pred(100200604004)