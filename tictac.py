from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import OneLineListItem
from kivymd.toast import toast
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import *
from kivymd.uix.label import *
from kivy.uix.image import *
from kivy.uix.screenmanager import *
from kivy.lang import Builder
from kivy.core.text import LabelBase 
from kivymd.uix.button import *
from kivymd.uix.screen import *
from kivymd.uix.textfield import *
from kivy.core.audio import *
from kivymd.uix.list import *
from kivymd.toast import *
from kivy.uix.scrollview import *
import requests
import webbrowser
import os
import subprocess
import sys
import threading
from pathlib import Path
from kivy.clock import Clock
from functools import partial
from kivymd.icon_definitions import md_icons
from kivy.utils import platform
from kivy.core.window import Window
import time
import _thread

Buil_strng ='''
ScreenManager:
    First:
    Setting:
        
        
        
<First>:
    name: 'first'
    MDIconButton:
        icon: 'arrow-left-circle-outline'
        pos_hint:{'center_x':0.1,'center_y':0.95}
        size_hint_y :0.05
        size_hint_x : 0.05
        on_press:
            root.manager.current = 'first'
        
    MDIconButton:
        icon: 'cog-outline'
        pos_hint:{'center_x':0.9,'center_y':0.95}
        size_hint_y :0.05
        size_hint_x : 0.05
        on_press:
            root.manager.current = 'setting'
        
    MDLabel:
        id: head
        text: '      Tic Tac Toe'
        text_color : 0,99/255, 76/255,1
        font_size : "40sp"
        pos_hint:{'center_x':0.5,'center_y':0.95}
                
    MDRectangleFlatButton:
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        #line_color: 0, 0, 1, 1
        #MDRaisedButton:
        id: userX
        text: "X"
        #icon: 'alpha-x-box'
        font_size: "50sp"
        pos_hint:{'center_x':0.2,'center_y':0.80}
        on_release: app.select(userX)
            
    MDRectangleFlatButton:
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        #line_color: 0, 0, 1, 1
        #icon: 'alpha-x-box'
        font_size: "50sp"
        id: userO
        text: "O"
        #icon: 'alpha-o-box'
        font_size: "50sp"
        pos_hint:{'center_x':0.8,'center_y':0.80}
        on_release: app.select(userO)
        
    MDRectangleFlatButton:
        id: btn1
        text: ""
        #md_bg_color: 1, 0, 1, 1
        size_hint: .3,.12
        pos_hint:{'center_x':0.2,'center_y':0.58}
        font_size : "80sp"
        on_release: app.r(btn1)
    MDRectangleFlatButton:
        id: btn2
        text: ""
        #md_bg_color: 1, 0, 1, 1
        size_hint: .3,.12
        pos_hint:{'center_x':0.5,'center_y':0.58}
        font_size : "80sp"
        on_release: app.r(btn2)
    MDRectangleFlatButton:
        id: btn3
        text: ""
        #md_bg_color: 1, 0, 1, 1
        size_hint: .3,.12
        pos_hint:{'center_x':0.8,'center_y':0.58}
        font_size : "80sp"
        on_release: app.r(btn3)
    MDRectangleFlatButton:
        id: btn4
        text: ""
        #md_bg_color: 1, 0, 1, 1
        size_hint: .3,.12
        pos_hint:{'center_x':0.2,'center_y':0.46}
        font_size : "80sp"
        on_release: app.r(btn4)
    MDRectangleFlatButton:
        id: btn5
        text: ""
        #md_bg_color: 1, 0, 1, 1
        size_hint: .3,.12
        pos_hint:{'center_x':0.5,'center_y':0.46}
        font_size : "80sp"
        on_release: app.r(btn5)
    MDRectangleFlatButton:
        id: btn6
        text: ""
        #md_bg_color: 1, 0, 1, 1
        size_hint: .3,.12
        pos_hint:{'center_x':0.8,'center_y':0.46}
        font_size : "80sp"
        on_release: app.r(btn6)
    MDRectangleFlatButton:
        id: btn7
        text: ""
        #md_bg_color: 1, 0, 1, 1
        size_hint: .3,.12
        pos_hint:{'center_x':0.2,'center_y':0.34}
        font_size : "80sp"
        on_release: app.r(btn7)
    MDRectangleFlatButton:
        id: btn8
        text: ""
        #md_bg_color: 1, 0, 1, 1
        size_hint: .3,.12
        pos_hint:{'center_x':0.5,'center_y':0.34}
        font_size : "80sp"
        on_release: app.r(btn8)
    MDRectangleFlatButton:
        id: btn9
        text: ""
        #md_bg_color: 1, 0, 1, 1
        size_hint: .3,.12
        pos_hint:{'center_x':0.8,'center_y':0.34}
        font_size : "80sp"
        on_release: app.r(btn9)
        
    MDFillRoundFlatButton:
        #icon:''
        id: reset
        text: "RESET"
        #size_hint: .3,.12
        pos_hint:{'center_x':0.5,'center_y':0.10}
        font_size : "18sp"
        on_release: app.reset()
    
    MDLabel:
        id: winlos
        text: ''
        text_color : 0,99/255, 76/255,1
        font_size : "32sp"
        pos_hint:{'center_x':0.8,'center_y':0.20}
                
<Setting>:
    name: 'setting'   
    MDIconButton:
        icon: 'arrow-left-circle-outline'
        pos_hint:{'center_x':0.1,'center_y':0.95}
        size_hint_y :0.05
        size_hint_x : 0.05
        on_press:
            root.manager.current = 'first'
        
    MDIconButton:
        icon: 'cog-outline'
        pos_hint:{'center_x':0.9,'center_y':0.95}
        size_hint_y :0.05
        size_hint_x : 0.05
        on_press:
            root.manager.current = 'setting'
        
    MDLabel:
        id: head
        text: '      Tic Tac Toe'
        text_color : 0,99/255, 76/255,1
        font_size : "40sp"
        pos_hint:{'center_x':0.5,'center_y':0.95}                     
    TwoLineIconListItem:
        text : '    Developer by:'
        secondary_text : '       Krishna Borase(Kriss)'
        pos_hint : {"center_x":0.3,"center_y":0.85}
                        
    TwoLineIconListItem:
        text : '    Version:'
        secondary_text : '        v1.8.0'
        pos_hint : {"center_x":0.3,"center_y":0.75}                   

    TwoLineIconListItem:
        text : '    Light Theme'
        secondary_text : '        Cllick for dark thim'
        pos_hint : {"center_x":0.3,"center_y":0.65} 
        on_release: app.light_thm()
              
    TwoLineIconListItem:
        text : '    Dark Theme'
        secondary_text : '        Cllick for dark thim'
        pos_hint : {"center_x":0.3,"center_y":0.55} 
        on_release: app.dark_thm()
    '''         
 
class First(Screen):
    pass       
class Setting(Screen):
    pass           
                                                                        
sm = ScreenManager()
sm.add_widget(First(name='first'))
sm.add_widget(Setting(name='setting'))


class TicTac(MDApp):
    user = ''
    not_user = ''
    i = 0
    
    def build(self):
        #self.theme_cls.theme_style = 'Dark'
        self.strng = Builder.load_string(Buil_strng)
        
        return self.strng
        
    def select(self,user):
        if user.text == 'X':
            #self.root.ids.userO.disabled = True
            self.user = 'X'
            #self.not_user = 'O'
        elif user.text == 'O':
            #self.root.ids.userX.disabled = True
            self.user = 'O'
            #self.not_user = 'X'

    def r(self,text):
        if text.text == "" and self.user != "":
            if self.i % 2 == 0:
                text.text = self.user
            else:
                text.text = self.not_user
        self.i += 1
        
        if self.user != "":
            if self.strng.get_screen('first').ids.btn1.text == self.user and self.strng.get_screen('first').ids.btn2.text == self.user and self.strng.get_screen('first').ids.btn3.text == self.user:
                self.strng.get_screen('first').ids.winlos.text=(f"{self.user} is Win!!!")

            elif self.strng.get_screen('first').ids.btn4.text == self.user and self.strng.get_screen('first').ids.btn5.text == self.user and self.strng.get_screen('first').ids.btn6.text == self.user:
                self.strng.get_screen('first').ids.winlos.text=(f"{self.user} is Win!!!")
                
            elif self.strng.get_screen('first').ids.btn7.text == self.user and self.strng.get_screen('first').ids.btn8.text == self.user and self.strng.get_screen('first').ids.btn9.text == self.user:
                self.strng.get_screen('first').ids.winlos.text=(f"{self.user} is Win!!!")
                
            elif self.strng.get_screen('first').ids.btn1.text == self.user and self.strng.get_screen('first').ids.btn4.text == self.user and self.strng.get_screen('first').ids.btn7.text == self.user:
                self.strng.get_screen('first').ids.winlos.text=(f"{self.user} is Win!!!")

            elif self.strng.get_screen('first').ids.btn2.text == self.user and self.strng.get_screen('first').ids.btn5.text == self.user and self.strng.get_screen('first').ids.btn8.text == self.user:
                self.strng.get_screen('first').ids.winlos.text=(f"{self.user} is Win!!!")
                
            elif self.strng.get_screen('first').ids.btn3.text == self.user and self.strng.get_screen('first').ids.btn6.text == self.user and self.strng.get_screen('first').ids.btn9.text == self.user:
                self.strng.get_screen('first').ids.winlos.text=(f"{self.user} is Win!!!")
                
            elif self.strng.get_screen('first').ids.btn1.text == self.user and self.strng.get_screen('first').ids.btn5.text == self.user and self.strng.get_screen('first').ids.btn9.text == self.user:
                self.strng.get_screen('first').ids.winlos.text=(f"{self.user} is Win!!!")

            elif self.strng.get_screen('first').ids.btn3.text == self.user and self.strng.get_screen('first').ids.btn5.text == self.user and self.strng.get_screen('first').ids.btn7.text == self.user:
                self.strng.get_screen('first').ids.winlos.text=(f"{self.user} is Win!!!")
                
           
    def reset(self):
        self.strng.get_screen('first').ids.btn1.text=("")
        self.strng.get_screen('first').ids.btn2.text=("")
        self.strng.get_screen('first').ids.btn3.text=("")
        self.strng.get_screen('first').ids.btn4.text=("")
        self.strng.get_screen('first').ids.btn5.text=("")
        self.strng.get_screen('first').ids.btn6.text=("")
        self.strng.get_screen('first').ids.btn7.text=("")
        self.strng.get_screen('first').ids.btn8.text=("")
        self.strng.get_screen('first').ids.btn9.text=("")
        
        self.strng.get_screen('first').ids.winlos.text=''
    
        
    def dark_thm(self):
        self.theme_cls.theme_style = 'Dark'
    def light_thm(self):
        self.theme_cls.theme_style = 'Light'

TicTac().run()                                                                          