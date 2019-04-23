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
#from PIL import Image2 



url = "https://digitalworldf08g2.firebaseio.com/"
apikey = "AIzaSyDHyug6TDWAda_ZirZ1G7B9cFV525ahvyk"

config = {
    "apiKey": apikey,
    "databaseURL": url,
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

from Database_handler import OrderHandler
from menu_handler import menuhandler
from trendline_handler import trend_handler


####This is the database handler

dbhandler= OrderHandler(db,'japanese_stall')
print(dbhandler.get_all_order())

###


#This is the menu handle

detail={                            # to be set by menu maker
	'EST_waiting_time':10,
	'price':5.50
}
foodname="Chicken with Rice"       #also set by menu maker
menu= menuhandler(db,'Indian')  
menu.new_item('ricc_with_noodle2.jpg',foodname,detail ) 
print("about to give menu")
a=menu.get_menu()
menu.get_photo("ricc_with_noodle2.jpg")
#end of menu handler


#trendline handler
trend=trend_handler(db)
sales=trend.get_sales()
print(sales)
popular=trend.get_popular()
print("printing trend")
print(popular)

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
        id: box
        orientation: "vertical"
        Label:
            text:"Menu"
        Button:
            background_color: 0, 0, 0, 0
            size_hint: 0.14,0.32
            pos_hint: {"center_y":0.5, "right":0.14}
            on_press: app.root.current = "screen_5"
            Image:
                source: "button11.png"
                keep_ratio: False
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: self.parent.size
                allow_stretch: True  
        ScrollView:
            id: scroll
            
            GridLayout:
                id: grid
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
        id: box
        orientation: "vertical"
        Label:
            text:"Menu"
        Button:
            background_color: 0, 0, 0, 0
            size_hint: 0.14,0.32
            pos_hint: {"center_y":0.5, "right":0.14}
            on_press: app.root.current = "screen_5"
            Image:
                source: "button11.png"
                keep_ratio: False
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: self.parent.size
                allow_stretch: True  
        
    
    
                    """)
class loginScreen(Screen):
    pass

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
        

sm=ScreenManager()
sm.add_widget(loginScreen())
sm.add_widget(fourScreen())
sm.add_widget(fiveScreen())
sm.add_widget(dashScreen())
sm.add_widget((menuScreen()))

a=receiveScreen()

#b=BoxLayout()
"""
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
"""


#a.ids[]
g=GridLayout(padding=20,spacing=50,cols=1,size_hint_y=None)
#commented out this property: ,height=GridLayout().minimum_height
#add labels for each order
l1=Label(text="First piece of text")
#l2=Label(text="Second Piece of text")
b=a.ids["box"]

s=ScrollView(id='scroll')

g.add_widget(l1)
#but=Button(size_hint=(0.14,0.15),pos_hint={"center_y":0.5, "right":0.17},on_press=change_screen_5)
#g.add_widget(Image(source="button11.png",keep_ratio=False,center_x=but.center_x,center_y=but.center_y,size=but.size))
#g.add_widget(but)
#g.add_widget(l2)


lis=dbhandler.get_all_order()
keys1=list(lis.keys())
for i in range(1,len(list(keys1))):
    dic=lis[keys1[i]]
    keys2=list(dic.keys())
    vals2=list(dic.values())
    
    g.add_widget(Label(text="Order number: "+keys1[i]))
    readyfn=partial(dbhandler.update,"ready",keys1[i])
    cookingfn=partial(dbhandler.update,"cooking",keys1[i])
    collectedfn=partial(dbhandler.update,"collected",keys1[i])
    but1=Button(text="ready",on_press=readyfn)
    g.add_widget(but1)
    but2=Button(text="cooking",on_press=cookingfn)
    g.add_widget(but2)
    but3=Button(text="collected",on_press=collectedfn)
    g.add_widget(but3)
    for j in range(len(keys2)):
        g.add_widget(Label(text=str(keys2[j])+":"+str(vals2[j]),halign="left"))
    

s.add_widget(g)
b.add_widget(s)
sm.add_widget(a)

class TutorialApp(App):
    
    def build(self):
        
        return sm
a=TutorialApp()
if __name__=="__main__":
    a.run()

