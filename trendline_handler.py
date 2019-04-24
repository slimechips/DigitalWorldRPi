from libdw import pyrebase
import datetime


class trend_handler:
	def __init__(self, db,store):
		#the object takes in two parameters, the name of the store and a database object 
		self.db=db
		self.store=store
	def get_popular(self):
		#The function is to get the sales of each item in the store
		all_items={} #
		complete=self.db.child('completed_orders').child(self.store).get()
		for entry in complete.each():
			items = entry.val()['food_item']
			if items in all_items:
				all_items[items]+=1 # if the item exist in the dictionary 
			else:
				all_items[items]=1# if the item does not exist, it means that the 
		return all_items
	def get_sales (self):
		sale=[]
		complete=self.db.child('completed_orders').child(self.store).get()
		for entry in complete.each():
			#collect the time of the order base of time of collection 
			date_time_str=entry.val()['time_of_order_collection']
			# make the datetime string  into datetime format for
			date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
			 # make the object into datetime format for each sorting
			items = entry.val()['food_item']
			# get the price usin the food itemm order
			price = db.child('menu').child('western_stall').child(items).child('price').get()#the price of the item
			sale.append([[date_time_obj.year,date_time_obj.month,date_time_obj.day],float(price.val()[1:])])
		return sale# return 2d array 
