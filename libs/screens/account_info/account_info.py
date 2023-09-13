
#start_import
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class AccountInfo(Screen):
    #start_ObjectProperty
    account_info = ObjectProperty(None) 
                