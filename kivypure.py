from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import matplotlib.pyplot as plt
import numpy as np


from libdw import pyrebase
import datetime
import json 
url = "https://digitalworldf08g2.firebaseio.com/"
apikey = "AIzaSyDHyug6TDWAda_ZirZ1G7B9cFV525ahvyk"

config = {
    "apiKey": apikey,
    "databaseURL": url,
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

x=db.child('active_orders').child('western_stall').child('order_000001').get()

    
class OrderHandler():
    def __init__(self,database,store_name):
        self.db= database
        self.store=store_name
        self.time_stamp= lambda: str(datetime.datetime.now()).split('.')[0]
    def update(self, status,order_number):
        completed={}
        if status=='ready':
            self.db.child('active_orders').child(self.store).child('order_000001').update({"status":status})
            self.db.child('active_orders').child(self.store).child('order_000001').update({"time_of_order_completion":self.time_stamp()}) 

        elif status=='collected':
            self.active=self.db.child('active_orders').child('western_stall').child(order_number).get()
            self.complete=self.db.child('completed_orders').child('western_stall').child(order_number)
            for entry  in self.active.each():
                print(entry.key(),entry.val())
                if entry.key()=='status':
                    completed['status']='collected'
                elif entry.key()=='time_of_order_collection':
                    completed['time_of_order_collection']=self.time_stamp()
                else:
                    completed[entry.key()]=entry.val()
            self.complete.set(completed)
            self.active=self.db.child('active_orders').child(self.store).child(order_number).remove()
            return completed
    def get_all_order(self):
        orders=[]
        stores=self.db.child('active_orders').child(self.store).get()
        for entry in stores.each():
            orders.append(entry.key())
        return orders

dbhandler= OrderHandler(db,'western_stall')

print(dbhandler.get_all_order())












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
<loginScreen>:
                
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
            
            size_hint: None, None
            text:"Enter username/email"
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
            text:"Enter password"
            #on_enter: app.root.current = "main_screen"
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.5,"center_y":0.4}
        Button:
            text: "Enter details"
            size_hint: None, None
            height: 30
            width: 120
            on_press: app.root.current = "screen_5" 
            pos_hint: {"center_x":0.5, "center_y":0.35}
        Button:
            text: "Create account"
            size_hint: None, None
            height: 30
            width: 120
            on_press: app.root.current = "signup" 
            pos_hint: {"center_x":0.5, "center_y":0.30}


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
            size_hint: 0.2,0.2
            pos_hint: {"center_y":0.5, "right":0.25}
            on_press: app.root.current = "login"
            Image:
                source: "button1.png"
                keep_ratio: False
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: self.parent.size
                allow_stretch: True
        Button:
            size_hint: 0.2,0.2
            pos_hint: {"center_y":0.5, "right":0.95}
            on_press: app.root.current = "screen_5"
            Image:
                source: "button2.png"
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
        orientation: "horizontal"

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
            size_hint: 0.2,0.2
            pos_hint: {"center_y":0.5, "left":0}
            on_press: app.root.current = "screen_5"
            Image:
                source: "button1.png"
                keep_ratio: False
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: self.parent.size
                allow_stretch: True 
        Button:
            size_hint: 0.2,0.2
            pos_hint: {"center_y":0.5, "right":1}
            on_press: app.root.current = "login"
            Image:
                source: "button2.png"
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
            pos_hint: {"center_x":0.15,"center_y":0.87}
        Label:
            size_hint: None, None
            text:"Sales Performance over time"
            color: 0,0,0,1
            write_tab: False
            multiline: False
            #on_text_validate: app.root.current = "main_screen" 
            height: 30
            width: 160
            pos_hint: {"center_x":0.65,"center_y":0.87}
        Image:
            source: "foo.png"
            pos_hint: {"center_x":0.72,"center_y":0.65}
            size_hint: (.4,.4)
            
        Label:
            size_hint: None, None
            text:"Average Sales last Month"
            color: 0,0,0,1
            write_tab: False
            multiline: False
            height: 30
            width: 160
            pos_hint: {"center_x":0.15,"center_y":0.37}
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
            pos_hint: {"center_x":0.65,"center_y":0.4}
<menuScreen>:
    name: 'menu'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: 'backnew.png'
            pos: 0,0
            size: self.width,self.height
        Rectangle:
            source: 'download.jpg'
            pos: 0,self.height/1.5
            size: self.width,self.height/3.
          
    BoxLayout:
        orientation: "vertical"
        
                

        Label:
            text:"Menu"
        Button:
            size_hint: 0.2,0.2
            pos_hint: {"y":-2, "left":0}
            on_press: app.root.current = "screen_5"
            Image:
                source: "button1.png"
                keep_ratio: False
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: self.parent.size
                allow_stretch: True  
        ScrollView:
            
            GridLayout:
                pos_hint: {"center_x":0.5,"center_y":0.9}
                padding: 20
                spacing: 10
                cols: 1
                # set GridLayout to be unrestricted vertically
                size_hint_y:  None
                # set the height of the layout to the combined height of the children
                height: self.minimum_height
                               
                
                Label:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    size_hint_y: None
                    height: '29sp'
                    hint_text: 'Firstname'
                TextInput:
                    hint_text: 'Surname'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    hint_text: 'Email'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    hint_text: 'Phone'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    size_hint_y: None
                    height: '29sp'
                    hint_text: 'Firstname'
                TextInput:
                    hint_text: 'Surname'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    hint_text: 'Email'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    hint_text: 'Phone'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    size_hint_y: None
                    height: '29sp'
                    hint_text: 'Firstname'
                TextInput:
                    hint_text: 'Surname'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    hint_text: 'Email'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    hint_text: 'Phone'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    size_hint_y: None
                    height: '29sp'
                    hint_text: 'Firstname'
                TextInput:
                    hint_text: 'Surname'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    hint_text: 'Email'
                    size_hint_y: None
                    height: '29sp'
                TextInput:
                    hint_text: 'Phone'
                    size_hint_y: None
                    height: '29sp'
                
<receiveScreen>:
    name: 'receive'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            source: 'backnew.png'
            pos: 0,0
            size: self.width,self.height
    BoxLayout:    
        orientation: "vertical"
        ScrollView:
            
            GridLayout:
                pos_hint: {"center_x":0.5,"center_y":0.5}
                padding: 20
                spacing: 10
                cols: 1
                # set GridLayout to be unrestricted vertically
                size_hint_y:  None
                # set the height of the layout to the combined height of the children
                height: self.minimum_height
            
                Label:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    text: 'Firstname'
                Label:
                    text: 'Surname'
                Label:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    text: 'Firstname'
                Label:
                    text: 'Surname'
                Label:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    text: 'Firstname'
                Label:
                    text: 'Surname'
                Label:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    text: 'Firstname'
                Label:
                    text: 'Surname'
                Label:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    text: 'Firstname'
                Label:
                    text: 'Surname'
                Label:
                    # cause the Layout's height is calculated by the children's height
                    # we have to disable size_hint_y and manually provide height
                    text: 'Firstname'
                Label:
                    text: 'Surname'
                    """)
class loginScreen(Screen):
    pass

class fourScreen(Screen):
    pass
class fiveScreen(Screen):
    pass
class dashScreen(Screen):
    pass
class menuScreen(Screen):
    pass
class receiveScreen(Screen):
    def update(self,w):
        self.add_widget(w)

sm=ScreenManager()
sm.add_widget(loginScreen())
sm.add_widget(fourScreen())
sm.add_widget(fiveScreen())
sm.add_widget(dashScreen())
sm.add_widget((menuScreen()))


lis=dbhandler.get_all_order()

a=receiveScreen()

for i in range(len(lis)):
    w=Label(text=lis[i],pos_hint= {"center_x":0.1,"center_y":0.9-(i)/(len(lis))})
    a.update(w)

sm.add_widget(a)

class TutorialApp(App):
    def build(self):
        
        return sm
a=TutorialApp()
if __name__=="__main__":
    a.run()

