from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.core.text import LabelBase
from typing import Union
from kivymd.uix.pickers import MDColorPicker
Window.size = (300, 600)
from libs.windowsmanage.windowsmanager import WindowsManager
import hashlib
import json
from kivy.properties import StringProperty

class MizdegzMarket(MDApp):
    def build(self):
        self.load_all_kv_files()
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Cyan'

        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.accent_hue = '400'
        # self.theme_cls.theme_style = 'Dark'
        #LabelBase.register(name='NunitoItalic', fn_regular='assets/Nunito/Nunito-Italic-VariableFont_wght.ttf')

        # تنظیم فونت برای Text و SecondaryText
       # self.theme_cls.font_styles['Custom'] = ['NunitoItalic', 16, False, 0.15]
        # self.theme_cls.theme_style = "Dark"
        self.root = Builder.load_file("libs/windowsmanage/windows_manager.kv")

    def Hash(self, data):
        # json baray hefz shekl data sakhter
        return hashlib.sha256(
            json.dumps(data, sort_keys=True).encode()
        ).hexdigest()

    def style_manage(self, self_color):
        if self.theme_cls.theme_style == "Light":
            if self_color:
                return self_color

        else:
            return 0, 0, 0, 0

    def load_all_kv_files(self) -> None:
        kv_files = [
            "libs/screens/login/login.kv",
            "libs/screens/authentication_code/authentication_code.kv",
            "libs/screens/wellcome/wellcome.kv",
            "libs/screens/account_info/account_info.kv",
            "libs/screens/main_screen/main_screen.kv",
            "libs/screens/shop/shop.kv",

        ]
        for kv in kv_files:
            self.load_kv(kv)

    def theme_style(self):

        if self.theme_cls.theme_style == "Light":
            self.theme_cls.primary_palette = "Indigo"
            self.theme_cls.theme_style = "Dark"
            Window.clearcolor = self.theme_cls.bg_darkest
        else:
            self.theme_cls.theme_style = "Light"
            Window.clearcolor = self.theme_cls.bg_normal
MizdegzMarket().run()