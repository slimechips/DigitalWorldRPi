import  barcode
import random
import os
from barcode.writer import ImageWriter
#from wand.image import Image
#from wand.display import display

# stall dish user
stalls=['Chicken Rice','Japanese']
dishes=[1,2,3,4,5,6,7,8,9,10]
sn=0
barcodeno=0
def barcode_generator(stallind,dishind,userid,date,time):

	# for i in stalls:
	# 	sn+=1
	# 	snstall='000'+str(sn)
	# 	print(snstall)
	# 	print(type(snstall))
	# for i2 in dishes:
	# 	snd+=1
	# 	if snd>=10:
	# 		sndish = '00'+str(snd)
	# 	else:
	# 		sndish = '000'+str(snd)
	# 	print(sndish)
	if dishind>=10:

		barcodeno=int('1'+ str(stallind) +str(dishind) + str(date)+ str(time) + str(userid))
		
	else:
		barcodeno=int('1'+ str(stallind) +str(dishind) + str(date)+ str(time)+ str(userid))

	image = barcode.get_barcode_class('ean13')
	image_bar = image(u'{}'.format(barcodeno),writer=ImageWriter())
	desktop = os.path.join(os.path.expanduser("~"), "Desktop")
	filePath = os.path.join(desktop, "test.png")
	f = open(filePath,'wb')
	image_bar.write(f)
	print(barcodeno)
	return barcodeno
	
	#add date time instead of the random numbers



barcode_generator(1,11,6854,2106,1010)