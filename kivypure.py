import os
import time
from kivy.uix.textinput import TextInput
os.environ['KIVY_GL_BACKEND']='gl'
from kivy.app import App
from kivy.uix.behaviors.knspace import knspace
def change_screen_5(*args):
    App.get_running_app().root.current = 'screen_5'
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
#from PIL import Image2 
from config import db
import camera

from Database_handler import OrderHandler
from menu_handler import menuhandler
from trendline_handler import trend_handler

fig = plt.figure()
ax1 = fig.add_subplot(111)

y=[1,4,9,16,25,36,49,64,81,100]
x=[1,2,3,4,5,6,7,8,9,10]
x = np.array(x)
y = np.array(y)
ax1.scatter(x, y,  c='b', marker="s", label='square')

plt.savefig('foo.png')

import matplotlib.pyplot as plt2
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt2.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt2.savefig('pie.png')



Builder.load_string("""
#:import Window kivy.core.window.Window
<loginScreen>:
    id: login_screen
    name: 'login'
    canvas:
        
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: 'login.jpg'
            pos: 0,0
            size: self.width,self.height
    FloatLayout:    
        TextInput:
            id: username
            size_hint: None, None
            text:""
            hint_text: 'Enter Username'
            #on_enter: app.root.current = "main_screen"
            write_tab: False
            multiline: False

            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.5}
        TextInput:
            id: password
            size_hint: None, None
            text:""
            hint_text: "Enter Password"
            #on_enter: app.root.current = "main_screen"
            write_tab: False
            multiline: False
            password: True
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.45}
        Button:
            text: "Enter details"
            size_hint: None, None
            height: 30
            width: 120
            on_press: login_screen.login_pressed()
            pos_hint: {"center_x":0.5, "center_y":0.35}

<fourScreen>:               
    name: 'signup'
    canvas:     
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: 'login.jpg'
            pos: 0,0
            size: self.width,self.height
    FloatLayout:  
        Button:
            size_hint: 0.14,0.15
            pos_hint: {"center_y":0.5, "right":0.17}
            on_press: app.root.current = "login"
            Image:
                source: "button11.png"
                keep_ratio: False
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: self.parent.size
                allow_stretch: True
        
        TextInput:
            size_hint: None, None
            text:"Enter registration email"
            #on_enter: app.root.current = "main_screen"
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.5}
        TextInput:
            size_hint: None, None
            text:"Enter password"
            #on_enter: app.root.current = "main_screen"
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.45}
        TextInput:
            size_hint: None, None
            text:"Re-enter password"
            #on_enter: app.root.current = "main_screen"
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.4}
        Button:
            text: "Confirm details"
            size_hint: None, None
            height: 30
            width: 120
            on_press: app.root.current = "screen_5" 
            pos_hint: {"center_x":0.5, "center_y":0.35}
<fiveScreen>:
    name: 'screen_5'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: 'backnew.png'
            pos: 0,0
            size: self.width,self.height
    FloatLayout:
        Button:
            size_hint: 0.14,0.15
            pos_hint: {"center_y":0.5, "right":0.17}
            on_press: app.root.current = "login"
            Image:
                source: "button11.png"
                keep_ratio: False
                center_x: self.parent.center_x-1
                center_y: self.parent.center_y
                size: self.parent.size
                allow_stretch: True

        Label:
            text: "Options"
        Button:
            size_hint: 0.2,0.6
            pos_hint: {"right":0.35,"center_y":0.5}
            text: "graphs"
            on_press: app.root.current = "menu"
            #size: self.parent.width/3,self.parent.height
            Image:
                source: "menu.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                #size_hint: self.parent.size_hint
                keep_ratio: False
                size: self.parent.size
                allow_stretch: True
        Button:
            size_hint: 0.2,0.6
            pos_hint: {"center_y":0.5, "center_x":0.5}
            text: "to screen 2"
            on_press: app.root.current = "dash"
            #size: self.parent.width/3,self.parent.height
            Image:
                source: "graph2.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                #size_hint: self.parent.size_hint
                keep_ratio: False
                size: self.parent.size
                allow_stretch: True
        Button:
            size_hint: 0.2,0.6
            pos_hint: {"center_y":0.5, "right":0.85}
            text: "to screen 2"
            on_press: app.root.current = "receive"
            #size: self.parent.width/3,self.parent.height
            Image:
                source: "order.png"
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                #size_hint: self.parent.size_hint
                keep_ratio: False
                size: self.parent.size
                allow_stretch: True
<dashScreen>:             
    name: 'dash'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: 'dash_clear.png'
            pos: 0,0
            size: self.width,self.height
    
    FloatLayout:
        Button:
            background_color: 0, 0, 0, 0
            size_hint: 0.14,0.2
            pos_hint: {"center_y":0.468, "right":0.16}
            on_press: app.root.current = "screen_5"
            Image:
                source: "dashbutton1.png"
                keep_ratio: False
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: self.parent.size
                allow_stretch: True 
        Label:
            size_hint: None, None
            text:"Top Selling Dishes"
            color: 0,0,0,1
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.25,"center_y":0.87}
        Label:
            size_hint: None, None
            text:"Sales Performance over time"
            color: 0,0,0,1
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.75,"center_y":0.87}
        Image:
            source: "foo.png"
            pos_hint: {"center_x":0.66,"center_y":0.65}
            size_hint: (.4,.4)
            
        Label:
            size_hint: None, None
            text:"Average Sales last Month"
            color: 0,0,0,1
            write_tab: False
            multiline: False
            height: 30
            width: 160
            pos_hint: {"center_x":0.25,"center_y":0.37}
        Label:
            size_hint: None, None
            text:""
            color: 0,0,0,1
            write_tab: False
            multiline: False
            height: 30
            width: 160
            pos_hint: {"center_x":0.15,"center_y":0.37}
        
        Image:
            source: "pie.png"
            pos_hint: {"center_x":0.72,"center_y":0.25}
            size_hint: (.25,.4)
        Label:
            size_hint: None, None
            text:"Sales Distribution"
            color: 0,0,0,1
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.75,"center_y":0.4}
            
<menuScreen>:
    name: "menu"
    id: menu_screen
    #current_stall: self.manager.current_stall
    canvas.before:
        
        Rectangle:
            id: rect_id
            source: 'backnew.png'
            pos: 0,0
            size: self.width,self.height
            
    # BoxLayout to contain top and bottom nav bars + contents of the screen
    BoxLayout:
        id: box
        orientation: "vertical"
        
        ScrollView:
            id: scroll
            size: self.size
            do_scroll_y: True
            
            # GridLayout to contain picture and label of food item
            GridLayout:
                id: grid
                cols: 3
                column_default_force: True
                column_default_width: Window.width/2
                height: self.minimum_height
                spacing: 80
                padding: 20
                size_hint_y: None
                
                Button:
                    id:but
                    size_hint: 0.33,None
                    
                    pos_hint: {'x': 0.35}
                    #pos_hint: {"center_y":0.5, "right":0.14}
                    on_press: app.root.current = "screen_5"
                    Image:
                        x: self.parent.x
                        y: self.parent.y
                        source: "button11.png"
                        keep_ratio: False
                        pos:self.pos
                        size: self.parent.size
                        allow_stretch: True
                        
                Widget:
                    
                Widget:
                    
<receiveScreen>:
    rect_id: 'rect_id'
    name: 'receive'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            id: rect_id
            source: 'backnew.png'
            pos: 0,0
            size: self.width,self.height
   
    BoxLayout:
        id:box
        orientation: "vertical"
        
        ScrollView:
            id:scroll
            size: self.size
            do_scroll_y: True
            
            # GridLayout to contain picture and label of food item
            GridLayout:
                id: grid
                cols: 3
                column_default_force: True
                column_default_width: Window.width/2
                height: self.minimum_height
                spacing: 20
                padding: 20
                size_hint_y: None
                
                Button:
                    id:but
                    size_hint: 0.33,None
                    
                    pos_hint: {'x': 0.35}
                    #pos_hint: {"center_y":0.5, "right":0.14}
                    on_press: app.root.current = "screen_5"
                    Image:
                        x: self.parent.x
                        y: self.parent.y
                        source: "button11.png"
                        keep_ratio: False
                        pos:self.pos
                        size: self.parent.size
                        allow_stretch: True
                        
                Widget:
                    
                Widget:
<adjustScreen>:
    name: 'adjust'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: 'backnew.png'
            pos: 0,0
            size: self.width,self.height
    FloatLayout:
        id:float
        Button:
            id:but
            size_hint: 0.33,None
            
            pos_hint: {'center_x':0.2,'center_y':0.8}
            #pos_hint: {"center_y":0.5, "right":0.14}
            on_press: app.root.current = "menu"
            Image:
                x: self.parent.x
                y: self.parent.y
                source: "button11.png"
                keep_ratio: False
                pos:self.pos
                size: self.parent.size
                allow_stretch: True
                        
        Widget:
            
        Widget:
            
        TextInput:
            id:name
            size_hint: None, None
            text:""
            hint_text: 'Enter Itemname'
            write_tab: False
            multiline: False

            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.5}
        TextInput:
            id:food_id
            size_hint: None, None
            text:""
            hint_text: "Enter food_id"
            #on_enter: app.root.current = "main_screen"
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.45}
        TextInput:
            id:price
            size_hint: None, None
            text:""
            hint_text: "Enter price"
            #on_enter: app.root.current = "main_screen"
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.4}
        
        TextInput:
            id:wait_time
            size_hint: None, None
            text:""
            hint_text: "Enter estimated wait time"
            #on_enter: app.root.current = "main_screen"
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.35}
<barcodeScreen>:
    name: 'barcode'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: 'backnew.png'
            pos: 0,0
            size: self.width,self.height
    FloatLayout:
        id:float
        Button:
            size_hint: 0.14,0.15
            pos_hint: {"center_y":0.5, "right":0.17}
            on_press: app.root.current = "login"
            Image:
                source: "button11.png"
                keep_ratio: False
                center_x: self.parent.center_x-1
                center_y: self.parent.center_y
                size: self.parent.size
                allow_stretch: True
        Label:
            size_hint: None, None
            text:"Scan Barcode to confirm the order"
            color: 0,0,0,1
            write_tab: False
            multiline: False 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.7}
        Label:
            id:lab1
            size_hint: None, None
            text:"Barcode not scanned yet"
            color: 0,0,0,1
            write_tab: False
            multiline: False
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.5}
                    """)

#s=ScrollView(id='scroll')
   
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
    pass
class fiveScreen(Screen):
    stall_name=loginhandler.cur_stall_user 
    pass
class dashScreen(Screen):
    stall_name=loginhandler.cur_stall_user 
    #def start(self):
        #Clock.schedule_interval(self., 10)
        
class menuScreen(Screen):
    array=[]
    def on_pre_leave(self,*args):
        super().on_leave(*args)
        for i in self.array:
            self.ids["grid"].remove_widget(i)
    def change(self,*args):
        self.parent.current="adjust"
    def on_enter(self,*args):
        super().on_enter(*args)
        stall_name=loginhandler.cur_stall_user 
        menu= menuhandler(db,stall_name) 
        menudic=menu.get_menu()
        titles=list(menudic.keys())
        menudicts=list(menudic.values())
        mgrid=self.ids["grid"]
        for i in range(len(titles)):
            title=titles[i]
            print("title is", title)
            menudict=menudicts[i]
            print("menu dictionary is",menudict)
            text=str(title)+"\n"+"Est. waiting time:"+str(menudict["est_waiting_time"])+"\n"+"Price:"+str(menudict["price"])
            #photo=menudict["photo_url"]
            url = menudict["photo_url"]
            w1=AsyncImage(source=url)
            self.array.append(w1)
            mgrid.add_widget(w1)
            l1=Label(text=text,size_hint_y=None,color=(0,0,0,1))
            self.array.append(l1)
            mgrid.add_widget(l1)
            screenmake=partial(self.change)
            but1=Button(size_hint= (None, None),text="Click to Edit",on_press=screenmake,pos_hint= {'x': 0.335})
            self.array.append(but1)
            mgrid.add_widget(but1)
        #self.interval=Clock.schedule_interval(self.on_enter, 10)

    def update(self,w):
        self.add_widget(w)
        
class Label1(Label):
    order_id=StringProperty()
    
class Button1(Button):
    order_id=StringProperty()

class receiveScreen(Screen):
    widgetlist=[]
    def change(self,*args):
        self.parent.current="barcode"
        
    def on_pre_leave(self,*args):
        super().on_leave(*args)
        self.interval.cancel()
    def on_enter(self,*args):
        super().on_enter(*args)
        stall_name=loginhandler.cur_stall_user 
        dbhandler= OrderHandler(db,stall_name)
        lis=dbhandler.get_all_order()
        keys1=list(lis.keys())
        
        for i in range(len((keys1))):
            g=self.ids["grid"]
            dic=(lis[keys1[i]])
            if(self.check(dic)==True):
                continue
            keys2=list(dic.keys())
            vals2=list(dic.values())
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
            empt=Widget(size_hint= (None, None))
            g.add_widget(empt)
            butmid=Button(size_hint=(None,None),id=keys1[i],text="Click to Scan Barcode",on_press=self.change)
            g.add_widget(butmid)
            empt1=Widget(size_hint= (None, None))
            g.add_widget(empt1)
            for i in [w1,w2,w3,but1,but2,but3]:
                self.widgetlist.append(i)
        
            #print("no orders")               
        self.interval=Clock.schedule_interval(self.on_enter, 10)
    def check(self,dic):
        flag=False
        for widget in self.widgetlist:
            if widget.order_id==str(dic["order_id"]):
                flag=True
        return flag
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
    def takeread(self,sm,*args):
        name=self.ids["name"].text
        food_id=int(self.ids["food_id"].text)
        price=self.ids["price"].text
        wait_time=self.ids["wait_time"].text
        dic={"est_waiting_time":wait_time,"food_id":food_id,"price":price}
        self.menu.update_detail(name,"est_waiting_time",wait_time)
        self.menu.update_detail(name,"food_id",food_id)
        self.menu.update_detail(name,"price",price)
        self.menu.update_detail(name, "stall_id", loginhandler.cur_stall_id)
        self.take_photo(name)

    def take_photo(self, name):
        name += ".jpg"
        camera.photo(name)
        stall_name=loginhandler.cur_stall_user 
        menu= menuhandler(db,stall_name)
        self.urlPath = menu.upload_photo(name, self.photo_uploaded)
        self.name = name

    def photo_uploaded(self, req, res, *args):
        self.menu.update_detail(self.name,"photo_url", self.urlPath)
        sm.current="menu"

        
        
class barcodeScreen(Screen):
    
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
        
    def change_screen(self,*args):
        self.manager.current=self.manager.previous()
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
        
            
        
        
        
    
sm=ScreenManager()
sm.add_widget(loginScreen())
sm.add_widget(fourScreen())
sm.add_widget(fiveScreen())
sm.add_widget(dashScreen())
sm.add_widget((receiveScreen()))
#Get the stall name from the username entered

#Declare order, menu and trend handlers

#trend = trend_handler(db,stall_name)  

#Declare the order screen to be modified using results from order handler
"""
a=receiveScreen()
b=a.ids["box"]
s=a.ids["scroll"]
g=a.ids["grid"]
"""
#Backend for Orders



#end of orders
"""
menuscreen=menuScreen()
mbox=menuscreen.ids["box"]
mscroll=menuscreen.ids["scroll"]
"""
#Menu handler
#imagepath='ricc_with_noodle2.jpg'

#menu.new_item(imagepath,foodname,detail ) 

#to loop
b=barcodeScreen()
sm.add_widget(b)
ad=adjustScreen()
sm.add_widget(menuScreen())
sm.add_widget(ad)

class TutorialApp(App):
    def build(self):
        return sm
a=TutorialApp()
if __name__=="__main__":
    a.run()

