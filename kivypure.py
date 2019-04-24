from kivy.app import App
from kivy.uix.behaviors.knspace import knspace
def change_screen_5(*args):
    App.get_running_app().root.current = 'screen_5'
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
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
import matplotlib.pyplot as plt
from libdw import pyrebase
import numpy as np
from functools import partial 
import loginhandler
#from PIL import Image2 
from config import db

from Database_handler import OrderHandler
from menu_handler import menuhandler
from trendline_handler import trend_handler


####This is the database handler

dbhandler= OrderHandler(db,'japanese_stall')
print(dbhandler.get_all_order())

###


#This is the menu handle




#a=menu.get_menu()
#menu.get_photo("ricc_with_noodle2.jpg")


#end of menu handler


#trendline handler
trend=trend_handler(db)
#sales=trend.get_sales()
#print(sales)
#popular=trend.get_popular()
#print("printing trend")
#print(popular)

#end of trendlline

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
            id: rect_id
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
        
    
                    """)

#s=ScrollView(id='scroll')
class loginScreen(Screen):
    def on_enter(self, *args):
        super().on_enter(*args)
        # Set clear the username and password fields
        self.ids["username"].text = ""
        self.ids["password"].text = ""

    def login_pressed(self, *args):
        # Login button pressed, check if credentials are correct
        username = self.ids["username"].text
        password = self.ids["password"].text
        cred_correct = loginhandler.check_credentials(username, password)
        if cred_correct:
            # Credentials correct, set current user and change screen
            self.ids["username"].background_color = [1, 1, 1, 1]
            self.ids["password"].background_color = [1, 1, 1, 1]
            loginhandler.cur_stall_user = username
            self.manager.current = "screen_5"
        else:
            # Credentials wrong, set text fields to red
            self.ids["username"].background_color = [1, 0.3, 0.3, 1]
            self.ids["password"].background_color = [1, 0.3, 0.3, 1]

class fourScreen(Screen):
    pass
class fiveScreen(Screen):
    pass
class dashScreen(Screen):
    def start(self):
        Clock.schedule_interval(self.change, 10)
        
class menuScreen(Screen):
    def start(self):
        Clock.schedule_interval(self.change, 10)
    def update(self,w):
        self.add_widget(w)

class receiveScreen(Screen):
    rect_id= ObjectProperty(None)
    def update(self,w):
        self.add_widget(w)
        (self.rect_id)

class adjustScreen(Screen):
    def takeread(self,menuhandler,sm,*args):
        name=self.ids["name"].text
        food_id=self.ids["food_id"].text
        price=self.ids["price"].text
        wait_time=self.ids["wait_time"].text
        dic={"est_waiting_time":wait_time,"food_id":food_id,"price":price}
        menuhandler.update_detail(name,"est_waiting_time",wait_time)
        menuhandler.update_detail(name,"food_id",food_id)
        menuhandler.update_detail(name,"price",price)
        sm.current="menu"
sm=ScreenManager()
sm.add_widget(loginScreen())
sm.add_widget(fourScreen())
sm.add_widget(fiveScreen())
sm.add_widget(dashScreen())


#b=BoxLayout()

#a.ids[]

#add labels for each order
l1=Label(text="First piece of text")
l1.bind(size=l1.setter("texture_size"))
#l2=Label(text="Second Piece of text")

a=receiveScreen()
b=a.ids["box"]
s=a.ids["scroll"]
g=a.ids["grid"]
#s=ScrollView(id='scroll',do_scrollable_y= True)
#,size_hint_y=None
#commented out this property: ,height=GridLayout().minimum_height
#but=Button(size_hint=(0.14,0.15),pos_hint={"center_y":0.5, "right":0.17},on_press=change_screen_5)
#g.add_widget(Image(source="button11.png",keep_ratio=False,center_x=but.center_x,center_y=but.center_y,size=but.size))
#g.add_widget(but)
#g.add_widget(l2)

#Backend for Orders

lis=dbhandler.get_all_order()
keys1=list(lis.keys())
for i in range(1,len(list(keys1))):
    dic=lis[keys1[i]]
    keys2=list(dic.keys())
    vals2=list(dic.values())
    text1="Item:"+str(dic["food_item"])+"\n"+"id:"+str(dic["food_id"])+"\n"+"Orders in Queue:"+str(dic["orders_in_queue"])+"\n"+"Special Requests:"+str(dic["special_requests"])
    text2="Est Waiting Time:"+str(dic["estimated_waiting_time"])+"\n"+"Time of Order:"+str(dic["time_of_order"])+"\n"+"Order Status:"+str(dic["status"])
    text3="Order ID:"+str(dic["order_id"])
    g.add_widget(Label(text=text1,size_hint_y=None,color=(0,0,0,1)))
    g.add_widget(Label(text=text2,size_hint_y=None,color=(0,0,0,1)))
    g.add_widget(Label(text=text3,size_hint_y=None,color=(0,0,0,1)))
    readyfn=partial(dbhandler.update,"ready",keys1[i])
    cookingfn=partial(dbhandler.update,"cooking",keys1[i])
    collectedfn=partial(dbhandler.update,"collected",keys1[i])
    but1=Button(size_hint= (None, None),text="ready",on_press=readyfn,pos_hint= {'x': 0.335})
    g.add_widget(but1)
    but2=Button(size_hint= (None, None),text="cooking",on_press=cookingfn,pos_hint= {'x': 0.335})
    g.add_widget(but2)
    but3=Button(size_hint= (None, None),text="collected",on_press=collectedfn,pos_hint= {'x': 0.335})
    g.add_widget(but3)

#end of orders
menuscreen=menuScreen()
mbox=menuscreen.ids["box"]
mscroll=menuscreen.ids["scroll"]
mgrid=menuscreen.ids["grid"]
#Menu handler

detail={                            # to be set by menu maker
	'EST_waiting_time':10,
    'key':7,
	'price':5.50
}
foodname="Chicken with Rice"       #also set by menu maker
#imagepath='ricc_with_noodle2.jpg'
menu= menuhandler(db,'chicken_rice_stall')  
#menu.new_item(imagepath,foodname,detail ) 
menudic=menu.get_menu()
titles=list(menudic.keys())
menudicts=list(menudic.values())
#to loop

ad=adjustScreen()
realtakeread=partial(ad.takeread,menu,sm)
ad.ids["float"].add_widget(Button(text="Enter details",size_hint=(None,None),height=30,width=120,pos_hint={"center_x":0.5, "center_y":0.30},on_press=realtakeread))

def change(*args):
    sm.current="adjust"

for i in range(1,len(titles)):
    title=titles[i]
    print("title is", title)
    menudict=menudicts[i]
    print("menu dictionary is",menudict)
    text=str(title)+"\n"+"Est. waiting time:"+str(menudict["est_waiting_time"])+"\n"+"Price:"+str(menudict["price"])
    #photo=menudict["photo_url"]
    w1=Button(background_color=(0,0,0,0))
    mgrid.add_widget(w1)
    mgrid.add_widget(Label(text=text,size_hint_y=None,color=(0,0,0,1)))
    screenmake=partial(change)
    but1=Button(size_hint= (None, None),text="Click to Edit",on_press=screenmake,pos_hint= {'x': 0.335})
    mgrid.add_widget(but1)

sm.add_widget(menuscreen)
sm.add_widget(ad)
sm.add_widget(a)

class TutorialApp(App):
    
    def build(self):
        return sm
a=TutorialApp()
if __name__=="__main__":
    a.run()

