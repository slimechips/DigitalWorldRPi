#Include necessary packages
import os
import time
from kivy.uix.textinput import TextInput
#os.environ['KIVY_GL_BACKEND']='gl'
from kivy.app import App
from kivy.uix.behaviors.knspace import knspace
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics.instructions import Canvas
from kivy.graphics import *
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import AsyncImage
import matplotlib.pyplot as plt
from libdw import pyrebase
import numpy as np
from functools import partial 
import loginhandler
from config import db
import camera
from multi_linear import pred_time
from Database_handler import OrderHandler
from menu_handler import menuhandler
from trendline_handler import trend_handler

#prepare new pie chart based on database



Builder.load_file('Kiv.kv')

#Define the different classes of screens for use later in ScreenManager.
class loginScreen(Screen):
    def on_enter(self, *args):
        super().on_enter(*args)
        # Set clear the username and password fields
        self.ids["username"].text = ""
        self.ids["password"].text = ""

        import os, ssl
        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context

    def login_pressed(self, *args):
        # Login button pressed, check if credentials are correct
        username = self.ids["username"].text
        password = self.ids["password"].text
        cred_correct, stall_id = loginhandler.check_credentials(username, password)
        if cred_correct and stall_id != None:
            # Credentials correct, set current user and change screen
            self.ids["username"].background_color = [1, 1, 1, 1]
            self.ids["password"].background_color = [1, 1, 1, 1]
            loginhandler.cur_stall_user = username
            loginhandler.cur_stall_id = stall_id
            self.manager.current = "screen_5"
        else:
            # Credentials wrong, set text fields to red
            self.ids["username"].background_color = [1, 0.3, 0.3, 1]
            self.ids["password"].background_color = [1, 0.3, 0.3, 1]

class fourScreen(Screen):
    stall_name=loginhandler.cur_stall_user 
    
class fiveScreen(Screen):
    stall_name=loginhandler.cur_stall_user 
    
class dashScreen(Screen):
    def on_enter(self,*args):
        #declare handlers
        stall_name=loginhandler.cur_stall_user 
        t=trend_handler(db,stall_name )
        pop=t.get_popular()
        sales=t.get_sales()
        #calculate metrics to use in graphs
        import matplotlib.pyplot as plt2
        labels = list(pop.keys())
        values = list(pop.values())
        c=100/(sum(values))
        sizes=[i*c for i in values]
        
        c=sorted(values)
        
        i3=max(c)
        for i in labels:
            if pop[i]==i3:
                max3=i
        self.ids["top3"].text=str(max3)
            
        fig1, ax1 = plt2.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt2.savefig('pie.png')
        print(sales)
        #prepare new bar chart based on database
        newdict={}
        for i in (sales):
            for j in list(pop.keys()):
                if j==i[2]:
                    newdict[j]=i[1]*pop[j]
        
        #find the total sales in the past month
        month=[]
        for i in sales:
            month.append(i[0][1])
        latest_month=max(month)
        month_sales=[]
        for i in sales:
            if i[0][1]==latest_month:
                month_sales.append(i[1])
        m_sales=sum(month_sales)
        self.ids["avg"].text=str(m_sales)
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        
        x=list(newdict.keys())
        y=list(newdict.values())
        ax1.bar(x,y)
        #save bar chart in a file
        plt.savefig('foo.png')
        
class menuScreen(Screen):
    array=[]
    #Removes widgets before leaving to ensure no extra widgets next time screen accessed
    def on_pre_leave(self,*args):
        super().on_leave(*args)
        for i in self.array:
            self.ids["grid"].remove_widget(i)
    #function to be bound to button to change screen
    def change(self,*args):
        self.parent.current="adjust"
    #function that includes all necessary widgets from database into menu screen everytime user enters screen
    def on_enter(self,*args):
        super().on_enter(*args)
        #declare handlers
        stall_name=loginhandler.cur_stall_user 
        menu= menuhandler(db,stall_name)
        #dictionary containing menu data
        menudic=menu.get_menu()
        titles=list(menudic.keys())
        menudicts=list(menudic.values())
        mgrid=self.ids["grid"]
        #loop through the dictionary of menu data
        for i in range(len(titles)):
            title=titles[i]
            menudict=menudicts[i]
            #Create text for label
            text=str(title)+"\n"+"Est. waiting time:"+str(menudict["est_waiting_time"])+"\n"+"Price:"+str(menudict["price"])
            url = menudict["photo_url"]
            w1=AsyncImage(source=url)
            self.array.append(w1)
            mgrid.add_widget(w1)
            l1=Label(text=text,size_hint_y=None,color=(0,0,0,1))
            self.array.append(l1)
            mgrid.add_widget(l1)
            #usage of partial function to pass function to on_press
            screenmake=partial(self.change)
            #create button that will change to edit screen
            but1=Button(size_hint= (None, None),text="Click to Edit",on_press=screenmake,pos_hint= {'x': 0.335})
            self.array.append(but1)
            mgrid.add_widget(but1)
    def update(self,w):
        self.add_widget(w)
#define custom label and button for identification through stringproperty(their ids are already taken up)        
class Label1(Label):
    order_id=StringProperty()
    
class Button1(Button):
    order_id=StringProperty()

#define screen that receives orders in real time
class receiveScreen(Screen):
    #declare widgetlist that will later allow identification of widgets to prevent repetition
    widgetlist=[]
    #define function to be bound to button to change screen to barcode screen
    def change(self,*args):
        self.parent.current="barcode"
    
    #define class behaviour right before leaving screen
    def on_pre_leave(self,*args):
        super().on_leave(*args)
        #cancels the clock declared in on_enter
        self.interval.cancel()
    #define function that helps to load new orders into the screen dynamically, using data structures from database and Clock
    def on_enter(self,*args):
        super().on_enter(*args)
        #declare handlers
        stall_name=loginhandler.cur_stall_user 
        dbhandler= OrderHandler(db,stall_name)
        #declare dictionary of all orders
        lis=dbhandler.get_all_order()
        keys1=list(lis.keys())
        #loop through the dictionary of orders
        for i in range(len((keys1))):
            #access g, the gridlayout inside the current screen
            g=self.ids["grid"]
            #access dictionary inside dictionary, containing data on current order
            dic=(lis[keys1[i]])
            if(self.check(dic)==True):
                continue
            keys2=list(dic.keys())
            vals2=list(dic.values())
            #create text for labels
            text1="Item:"+str(dic["food_item"])+"\n"+"id:"+str(dic["food_id"])+"\n"+"Orders in Queue:"+str(dic["orders_in_queue"])+"\n"+"Special Requests:"+str(dic["special_requests"])
            text2="Est Waiting Time:"+str(dic["estimated_waiting_time"])+"\n"+"Time of Order:"+str(dic["time_of_order"])+"\n"+"Order Status:"+str(dic["status"])
            text3="Order ID:"+str(dic["order_id"])
            w1=Label1(text=text1,size_hint_y=None,color=(0,0,0,1),order_id=str(dic["order_id"]))
            g.add_widget(w1)
            w2=Label1(text=text2,size_hint_y=None,color=(0,0,0,1),order_id=str(dic["order_id"]))
            g.add_widget(w2)
            w3=Label1(text=text3,size_hint_y=None,color=(0,0,0,1),order_id=str(dic["order_id"]))
            g.add_widget(w3)
            but1=Button1(size_hint= (None, None),text="ready",on_press=partial(self.butpres1,dbhandler,keys1[i]),pos_hint= {'x': 0.335},order_id=str(dic["order_id"]))
            g.add_widget(but1)
            but2=Button1(size_hint= (None, None),text="cooking",on_press=partial(self.butpres2,dbhandler,keys1[i]),pos_hint= {'x': 0.335},order_id=str(dic["order_id"]))
            g.add_widget(but2)
            but3=Button1(size_hint= (None, None),text="collected",on_press=partial(self.butpres3,dbhandler,keys1[i]),pos_hint= {'x': 0.335},order_id=str(dic["order_id"]))
            g.add_widget(but3)
            #declare empty widgets to fill up the space on the left and right of the barcode button
            empt=Widget(size_hint= (None, None))
            g.add_widget(empt)
            #bind change function to the middle button, allowing vendor to scan the barcodes
            butmid=Button(size_hint=(None,None),id=keys1[i],text="Click to Scan Barcode",on_press=self.change)
            g.add_widget(butmid)
            empt1=Widget(size_hint= (None, None))
            g.add_widget(empt1)
            #append the previous 6 widgets to the widgetlist, to access them later and previous potential repeats
            for i in [w1,w2,w3,but1,but2,but3]:
                self.widgetlist.append(i)
        
        #Schedule the entire function within a Clock
        self.interval=Clock.schedule_interval(self.on_enter, 10)
    #define function        
    #Checks if widget is in widgetlist    
    def check(self,dic):
        flag=False
        for widget in self.widgetlist:
            if widget.order_id==str(dic["order_id"]):
                flag=True
        return flag
    #function defining button behaviour for 1
    def butpres1(self,dbhandler,item,but1,*args):
        dbhandler.update("ready",item)
        i=self.widgetlist.index(but1)
        print(i)
        try:
            print("replacing")
            self.widgetlist[i-2].text=self.widgetlist[i-2].text.replace("cooking","ready")
            print("replaced?")
            print(self.widgetlist[i-2].text)
        except:
            pass
        try:
            self.widgetlist[i-2].text=self.widgetlist[i-2].text.replace("collected","ready")
        except:
            pass
        try:
            self.widgetlist[i-2].text=self.widgetlist[i-2].text.replace("sent","ready")
        except:
            pass
    #function defining button behaviour for 2
    def butpres2(self,dbhandler,item,but2,*args):
        dbhandler.update("cooking",item)
        i=self.widgetlist.index(but2)
        try:
            self.widgetlist[i-3].text=self.widgetlist[i-3].text.replace("collected","cooking")
        except:
            pass
        try:
            self.widgetlist[i-3].text=self.widgetlist[i-3].text.replace("ready","cooking")
        except:
            pass
        try:
            self.widgetlist[i-3].text=self.widgetlist[i-3].text.replace("sent","cooking")
        except:
            pass
        
    #function defining button behaviour for 3
    def butpres3(self,dbhandler,item,but3,*args):
        dbhandler.update("collected",item)
        i=self.widgetlist.index(but3)
        try:
            self.widgetlist[i-4].text=self.widgetlist[i-4].text.replace("cooking","collected")
        except:
            pass
        try:
            self.widgetlist[i-4].text=self.widgetlist[i-4].text.replace("ready","collected")
        except:
            pass
        try:
            self.widgetlist[i-4].text=self.widgetlist[i-4].text.replace("sent","collected")
        except:
            pass
    def start(self):
        Clock.schedule_interval(self.on_enter, 10)
    def update(self,w):
        self.add_widget(w)
        (self.rect_id)

#define class of screen in which Menu Items can be modified by vendor
class adjustScreen(Screen):
    def on_leave(self,*args):
        super().on_leave(*args)
        self.interval.cancel()
        
    def on_enter(self,*args):
        super().on_enter(*args)
        stall_name=loginhandler.cur_stall_user
        self.menu= menuhandler(db,stall_name)
        realtakeread=partial(self.takeread,self.menu,sm)
        self.ids["float"].add_widget(Button(text="Enter details",size_hint=(None,None),height=30,width=120,pos_hint={"center_x":0.5, "center_y":0.30},on_press=realtakeread))
        self.interval=Clock.schedule_interval(self.on_enter, 10)
    #Takes edits and sends them to the database   
    def takeread(self,sm,*args):
        name=self.ids["name"].text
        food_id=int(self.ids["food_id"].text)
        price=self.ids["price"].text
        wait_time=self.ids["wait_time"].text
        dic={"est_waiting_time":wait_time,"food_id":food_id,"price":price}
        self.menu.update_detail(name,"est_waiting_time",int(wait_time))
        self.menu.update_detail(name,"food_id",int(food_id))
        self.menu.update_detail(name,"price",price)
        self.menu.update_detail(name, "stall_id", int(loginhandler.cur_stall_id))
        self.urlPath = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png"
        self.menu.update_detail(name, "photo_url", "None")
        print("trying")
        self.take_photo(name)
    #takes photo from usb camera
    def take_photo(self, name):
        print("name", name)
        camera.photo(name + ".jpg")
        stall_name=loginhandler.cur_stall_user 
        menu= menuhandler(db,stall_name)
        self.urlPath = menu.upload_photo(name + ".jpg", self.photo_uploaded)
        self.name = name
    #uploads photo to database
    def photo_uploaded(self, req, res, *args):
        print("Photo Upload success!")
        self.menu.update_detail(self.name,"photo_url", self.urlPath + "?alt=media")
        sm.current="menu"
#Define class for barcode screen
class barcodeScreen(Screen):
    #Start a big text input, which will later update to correct or false depending on barcode scan
    def on_enter(self,*args):
        super().on_enter(*args)
        l=TextInput(on_text_validate=self.check_a, multiline=False,font_size=20)
        self.add_widget(l)
        self.leave = Clock.schedule_once(self.change_screen,15)
    def on_leave(self, *args):
        super().on_leave(*args)
        try:
            self.leave.cancel()
        except:
            pass
    #changes screen to previous one
    def change_screen(self,*args):
        self.manager.current=self.manager.previous()
    #checks if the number received by scanner is the same as the order id being compared against
    def check_a(self,instance,*args):
        self.a=instance.text
        print(self.a)
        stall_name=loginhandler.cur_stall_user 
        dbhandler= OrderHandler(db,stall_name)
        lis=dbhandler.get_all_order()
        keys1=list(lis.keys())
        self.a=str(self.a)[:-1]
        flag=False
        for i in keys1:
            if i==self.a:
                instance.text="Correct Barcode!"
                flag=True
                break
        if(flag==False):
            instance.text="Wrong Barcode!"
        self.leave.cancel()
        Clock.schedule_once(self.change_screen,5)
        
#declare screenmanager, all screens, add it to screen manager.
sm=ScreenManager()
sm.add_widget(loginScreen())

sm.add_widget(fourScreen())
sm.add_widget(fiveScreen())
d=dashScreen()
sm.add_widget(d)
sm.add_widget((receiveScreen()))

b=barcodeScreen()
sm.add_widget(b)
ad=adjustScreen()
sm.add_widget(menuScreen())
sm.add_widget(ad)

class KivApp(App):
    def build(self):
        return sm
a=KivApp()
if __name__=="__main__":
    a.run()

