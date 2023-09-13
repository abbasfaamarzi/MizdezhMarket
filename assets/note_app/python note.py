'''نوشتن یک تابع برای تبدلیل url به مسیر import را تولید کند'''

def convert_path_to_ky_syntax(path : str):
    from kivy.core.clipboard import Clipboard
    path1 = path.replace("/",".")
    path2 = path1.split(".")[:-1]
    kivy_file = path2[-1]
    path[-1] = path2[-1].replace("_","")
    Clipboard.copy(
        f"#:import {path2}"
    )
    print(path1)
    print(path2)
convert_path_to_ky_syntax("libs/screens/main_screen/main_screen.kv")