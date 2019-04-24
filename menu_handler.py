from libdw import pyrebase
import urllib
from PIL import Image 
class menuhandler():
	def __init__ (self,db,store):
		self.db=db
		self.store=store
	def update_detail(self, food_item, key, value):
		self.db.child('menu').child(self.store).child(food_item).child(key).set(value)
	def new_item(self,filename,food_name,food_details):
		items= self.db.child('menu').child(self.store).get()
		index= len(items.key())
		food_details['key']= index+1
		self.upload_file(filename)
		self.db.child('menu').child(self.store).child(food_name).set(food_details)

	def upload_file(self,filename):
	    my_file = open(filename, "rb")
	    my_bytes = my_file.read()
	    my_url = "https://firebasestorage.googleapis.com/v0/b/digitalworldf08g2.appspot.com/o/{}%2F{}".format(self.store,filename)
	    my_headers = {"Content-Type": "image/jpg"}

	    my_request = urllib.request.Request(my_url, data=my_bytes, headers=my_headers, method="POST")

	    try:
	        loader = urllib.request.urlopen(my_request)
	    except urllib.error.URLError as e:
	        message = json.loads(e.read())
	        print(message["error"]["message"])
	    else:
	        print(loader.read())
	def get_menu(self):
		r_msg={}
		menu_details = self.db.child('menu').child(self.store).get()
		for items in menu_details.each():
			print(items.key(),items.val())
			r_msg[items.key()]= items.val()
		return r_msg
	def get_photo(self, items): #items is filename with directory , with extension
		# the url is prefixed into  
		my_url = "https://firebasestorage.googleapis.com/v0/b/digitalworldf08g2.appspot.com/o/{}%2F{}?alt=media".format(self.store,items)
		print(my_url)
		try:
			loader = urllib.request.urlretrieve(my_url,items)

		except urllib.error.URLError as e:
			message = json.loads(e.read())
			print(message["error"]["message"])
		else:
			print(loader)

detail={                            # to be set by menu maker
	'EST_waiting_time':10,
	'price':5.50
}
foodname="Chicken with Rice"       #also set by menu maker
menu= menuhandler(db,'Indian')  

menu.update_detail('Chicken with Rice', 'price','40')

#imageblob.upload_from_filename(imagesPath)

#for new item, need dynamic filename, saves it, and uploads that one 

#widgets that ned to be dynamic