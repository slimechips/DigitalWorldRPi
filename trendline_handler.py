from libdw import pyrebase
import datetime
 


url = "https://digitalworldf08g2.firebaseio.com/"
apikey = "AIzaSyDHyug6TDWAda_ZirZ1G7B9cFV525ahvyk"

config = {
    "apiKey": apikey,
    "databaseURL": url,
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class trend_handler:
	def __init__(self, db):
		self.db=db
	def get_popular(self):
		all_items={} #
		complete=self.db.child('completed_orders').child('western_stall').get()
		for entry in complete.each():
			items = entry.val()['food_item']
			if items in all_items:
				all_items[items]+=1
			else:
				all_items[items]=1
		return all_items
	def get_sales (self):
		sales={}
		sale2=[]
		complete=self.db.child('completed_orders').child('western_stall').get()
		for entry in complete.each():

			date_time_str=entry.val()['time_of_order_collection']
			date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S') # make the object into datetime format for each sorting
			items = entry.val()['food_item']

			price = db.child('menu').child('western_stall').child(items).child('price').get()#the price of the item
			sale2.append([[date_time_obj.year,date_time_obj.month,date_time_obj.day],float(price.val()[1:])])
		return sale2# return 2d array 

trend=trend_handler(db)
sales=trend.get_sales()
print(sales)
popular=trend.get_popular()
print("printing trend")
print(popular)