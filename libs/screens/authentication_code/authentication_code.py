
#start_import
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class AuthenticationCode(Screen):
    #start_ObjectProperty
    auth_code_id = ObjectProperty(None)
                