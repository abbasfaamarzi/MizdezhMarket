
#start_import
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.app import App
from kivymd.uix.bottomsheet import MDListBottomSheet
from assets.note_app.note_dict import main_menu
class MainScreen(Screen):
    #start_ObjectProperty
    main_screen_id = ObjectProperty(None)
    shop_id = ObjectProperty(None)
    app = App.get_running_app()
    def set_menu(self):
        bottom_sheet_menu = MDListBottomSheet(radius_from = 'top', auto_dismiss = True,bg_color = self.app.theme_cls.primary_color if self.app.theme_cls.theme_style == 'Dark' else  self.app.theme_cls.bg_normal)
        for item in main_menu.items():
            bottom_sheet_menu.add_item(
            item[0].title(),
            lambda x, y=item[0]: self.callback_for_menu_items(y),
            icon=item[1],

            )
        bottom_sheet_menu.open()


    def callback_for_menu_items(self, item):
        print(item)
