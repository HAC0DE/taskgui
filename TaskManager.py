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
#from kivymd.uix.expansionpanel  MDExpansionPanel, MDExpansionPanelThreeLine
from functools import partial
from kivy.clock import Clock
from kivymd.toast import toast
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
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.picker import MDTimePicker,MDDatePicker
#import pygame
#from kivy.garden.notification import Notification


Buil_strng ='''
ScreenManager:
    First:
    Second:
    New:

<First>:
    name:'first'
    MDLabel:
        text:'  Task Maneger                        '
        #text_color: 1,1,1,1             
        halign: 'center'
        font_style: 'H5'
        #md_bg_color: 0,0,0,1
        size_hint_y :0.08
        size_hint_x : 0.99
        pos_hint:{'center_x':0.5,'center_y':0.96}
    ScrollView:
        MDList:
            pos_hint:{'center_x':0.5,'center_y':0.84}
            id:task_items
    MDTextField:
        id : task_text
        multiline: True
        size_hint:(0.9,0.1)
        pos_hint:{'center_x':0.5,'center_y':0.34}
        hint_text:'Enter your task '
    #MDLabel:
#        text:'Task'
#        halign: 'center'
#        font_style: 'H2'
#        pos_hint:{'center_y':0.8}
#    
    MDIconButton:
        icon: "check"
        #md_bg_color: 1,1,1,1
        pos_hint: {'center_x':0.9,'center_y':0.34}
        on_press:
            app.addTask()
    
    
    MDFloatingActionButton:
        icon: "plus"
        #md_bg_color: 1,1,1,1
        pos_hint: {'center_x':0.9,'center_y':0.43}
        on_press:
            app.new2do()
    
    #MDRaisedButton:
#        text:'Add task'
#        pos_hint: {'center_x':0.5,'center_y':0.35}
        
<Second>:
    name: 'second'
    MDLabel:
        text:'  Task Maneger                  '
        halign: 'center'
        font_style: 'H5'
        md_bg_color: 1,1,1,1
        size_hint_y :0.08
        size_hint_x : 0.99
        pos_hint:{'center_x':0.5,'center_y':0.96}
    ScrollView:
        MDList:
            id:task_items

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x':0.3,'center_y':0.2}
        on_press:
            root.manager.current = 'first'

<New>:
    name: 'new'
    MDLabel:
        text:'  New Task                          '
        halign: 'center'
        font_style: 'H5'
        md_bg_color: 1,1,1,1
        size_hint_y :0.08
        size_hint_x : 0.99
        pos_hint:{'center_x':0.5,'center_y':0.96}
    MDLabel:
        text:'       What is to be done?'
        halign: 'center'
        #font_style: 'H2'
        pos_hint:{'center_x':0.2,'center_y':0.89}
    MDTextField:
        id : task_text1
        #multiline: True
        size_hint:(0.9,0.1)
        pos_hint:{'center_x':0.5,'center_y':0.83}
        hint_text:'Enter your task'

    MDLabel:
        text:'Due date          '
        halign: 'center'
        #font_style: 'H2'
        pos_hint:{'center_x':0.2,'center_y':0.73}
    MDTextField:
        id : task_date
        #multiline: True
        size_hint:(0.9,0.1)
        pos_hint:{'center_x':0.5,'center_y':0.67}
        hint_text: 'Date not set'
        wieight:"25dp"
    MDIconButton:
        icon: "calendar"
        #md_bg_color: 1,1,1,1
        pos_hint: {'center_x':0.9,'center_y':0.67}
        on_press:
            app.show_time_picker()
    MDTextField:
        id : task_time
        #multiline: True
        size_hint:(0.9,0.1)
        pos_hint:{'center_x':0.5,'center_y':0.58}
        size_hint_y :0.10
        size_hint_x : 0.9
        hint_text: 'Time not set (all day)'
    MDIconButton:
        icon: "clock"
        #md_bg_color: 1,1,1,1
        pos_hint: {'center_x':0.9,'center_y':0.58}
        on_press:
            app.show_time_picker()

    MDLabel:
        text:'Notifications  '
        halign: 'center'
        #font_style: 'H2'
        pos_hint:{'center_x':0.2,'center_y':0.52}

    MDFloatingActionButton:
        icon: "check"
        #md_bg_color: 1,1,1,1
        pos_hint: {'center_x':0.9,'center_y':0.05}
        on_press:
            app.addTask2()

'''
class First(Screen):
    pass
class Second(Screen):
    pass
class New(Screen):
    pass

sm = ScreenManager()
sm.add_widget(First(name = 'first'))
sm.add_widget(Second(name = 'second'))
sm.add_widget(New(name = 'new'))

class NewApp(MDApp):
    
    #pygame.init()
#    sound = pygame.mixer.Sound('alarm.mp3')
#    volume = 0.5
    
    def build(self):
        self.strng = Builder.load_string(Buil_strng)
        
        return self.strng

    def addTask(self,):
        self.task_text = self.strng.get_screen('first').ids.task_text.text
        if self.task_text.split() != []:
            self.strng.get_screen('first').manager.current = 'first'
            self.strng.get_screen('first').ids.task_items.add_widget(
                TwoLineIconListItem(text = self.task_text,secondary_text='hi')
            )
            toast(text = 'Task Added')
        else:
            toast(text = 'Task is Empty')
 
    def addTask2(self,):
        self.task_text1 = self.strng.get_screen('new').ids.task_text1.text
        if self.task_text1.split() != []:
            self.strng.get_screen('new').manager.current = 'new'
            self.strng.get_screen('first').manager.current = 'first'
            self.strng.get_screen('first').ids.task_items.add_widget(
                TwoLineIconListItem(text = self.task_text1,secondary_text='hi')
            )
            toast(text = 'Task Added')
        else:
            toast(text = 'Task is Empty')    
       
    def new2do(self):
        self.strng.get_screen('new').manager.current = 'new'

    def on_save(self, instance, time):
        self.task_time = self.strng.get_screen('new').ids.task_time.text=str(time)
    
    def on_cancel(self, instance, time):
        self.task_time = self.strng.get_screen('new').ids.task_time.text=str(time)
        
    def show_time_picker(self):
        '''Open time picker dialog.'''

        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        time_dialog.open()
        
    

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()



NewApp().run()