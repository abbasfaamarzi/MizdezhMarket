
#start_import
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class Login(Screen):
    #start_ObjectProperty
    login_id = ObjectProperty(None)
    def check_phone(self, text):
        r = "Right Phone Number"
        if len(text) == 1:
            if text == "0":
                self.ids.phone_number.helper_text = r
            elif len(text) >=1 and text[0] == "0":
                self.ids.phone_number.helper_text = r
        else:
            self.ids.phone_number.helper_text = "Invalid Phone Number"