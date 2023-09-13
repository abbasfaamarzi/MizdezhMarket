from kivy.properties import ObjectProperty,ListProperty
from kivymd.toast import toast
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager,SlideTransition,FadeTransition
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
import webbrowser
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.app import App

class WindowsManager(ScreenManager):
    app = App.get_running_app()
    login_id = ObjectProperty(None)
    auth_code_id = ObjectProperty(None)
    wellcome_id = ObjectProperty(None)
    account_info_id = ObjectProperty(None)
    main_screen_id = ObjectProperty(None)
    def previous_screen(self) :
        self.change_screen(self.live_screen[-2])

    def change_screen(self, screen, slide_transition = None):
        self.transition = SlideTransition(direction=slide_transition) if slide_transition else FadeTransition()
        try:
            print(screen)
            self.live_screen.append(screen)
            self.current = screen
        except:
            print(f"not found {screen}")
    def check_on_press(self, instance):
        print(instance)

