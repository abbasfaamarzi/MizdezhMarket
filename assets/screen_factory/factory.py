
import os
import re
sc = r"C:\Users\user\PycharmProjects\cinix\libs\screens"
c = r"C:\Users\user\PycharmProjects\cinix\libs\components"
class SetImport:
    def __init__(self, path):
        self.component_name = path.split('\\')[-1].split('.')[0].title()
        self.path = os.path.dirname(
            path).split("\\")[5:]
        self.component_name = self.join_with_underscore()

    def join_with_underscore(self):
        self.path.append(self.path[-1])
        words = [i.title() for i in self.component_name.split("_")]
        joined_sentence = "".join(words)
        return joined_sentence
    def return_kv_path(self):
        return f"#:import {self.component_name} {'.'.join(self.path)}.{self.component_name}"

class ToolsStylePath:
    tools_path = r"C:\Users\user\PycharmProjects\pipe_genius\libs\components\tools_style\tools_style.py"
    def style_extract_classes(self, other = None):
        with open(other if other else self.tools_path , 'r') as file:
            content = file.read()

        class_pattern = re.compile(r'class\s+(\w+)')
        classes = class_pattern.findall(content)
        tools_style_path = "#_0tools_style_path\n"
        for style in classes:
            tools_style_path += f"#:import {style} {'.'.join(SetImport(other if other else self.tools_path).path)}.{style}\n"
        return tools_style_path + "#_0tools_style_path"



class WindowsManagerSetup:
    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.filename = r"C:\Users\user\PycharmProjects\pipe_genius\windows_manager\windows_manager.kv"
        self.set_screen()
        #self.py_set_property()
    def set_import(self):
        flag = '#start_import'
        screen_name1 = (self.screen_name.replace("_", " ").title()).split(" ")[0] + \
                       (self.screen_name.replace("_", " ").title()).split(" ")[1]
        with open(self.filename, 'r') as file:
            content = file.read()

        pattern = fr"{re.escape(flag)}(\s*\n)?"
        replaced_content = re.sub(pattern,
                                  fr"{flag}\n#:import {screen_name1} libs.screens.{self.screen_name}.{self.screen_name}.{screen_name1}\n",
                                  content)

        with open(self.filename, 'w') as file:
            file.write(replaced_content)
        return screen_name1
    def set_property(self):
        flag= '#start_ObjectProperty'
        id = self.screen_name + "_id"
        with open(self.filename, 'r') as file:
            content = file.read()

        pattern = fr"{re.escape(flag)}(\s*\n)?"
        replaced_content = re.sub(pattern, fr"{flag}\n    {id} : {id}\n", content)

        with open(self.filename, 'w') as file:
            file.write(replaced_content)
        return id
    def set_screen(self):
        flag= '#start_screens'
        screen_name = self.set_import()
        id = self.set_property()
        with open(self.filename, 'r') as file:
            content = file.read()

        pattern = fr"{re.escape(flag)}(\s*\n)?"
        replaced_content = re.sub(pattern, fr"{flag}\n    {screen_name}:\n        id : {id}\n", content)

        with open(self.filename, 'w') as file:
            file.write(replaced_content)
    def py_set_property(self):
        windows_manager_py = r"C:\Users\user\PycharmProjects\pipe_genius\windows_manager\windows_manager.py"
        flag= '#start_ObjectProperty'
        id1 = self.screen_name + "_id"
        with open(windows_manager_py, 'r') as file:
            content = file.read()

        pattern = fr"{re.escape(flag)}(\s*\n)?"
        replaced_content = re.sub(pattern, fr"{flag}\n    {id1} = ObjectProperty(None)\n", content)

        with open(self.filename, 'w') as file:
            file.write(replaced_content)


class ScreenFactory:
    def __init__(self, base_path, folder_name):
        self.base_path = base_path
        self.folder_name = folder_name
        self.base_path = self.base_path

        self.create_directory_with_files()

    def create_directory_with_files(self, inhrients = None):
        try:
            directory_path = os.path.join(self.base_path , self.folder_name)
            os.makedirs(directory_path)

            kv_file_path = os.path.join(directory_path, f"{self.folder_name}.kv")
            py_file_path = os.path.join(directory_path, f"{self.folder_name}.py")
            class_name = self.folder_name.capitalize()
            class_name_split = class_name.split("_")
            class_name = ""
            for i in class_name_split:
                class_name += i.title()
            with open(kv_file_path, 'w', encoding='utf-8') as kv_file:
                # نوشتن محتوای فایل kv
                kv_file.write(ToolsStylePath().style_extract_classes() + "\n")
                kv_file.write("#start_import\n")
                kv_file.write(f"<{class_name}>\n")
                kv_file.write("    #start_ObjectProperty\n")
                kv_file.write(f"    name : '{self.folder_name}'")
            with open(py_file_path, 'w', encoding='utf-8') as py_file:
                # نوشتن محتوای فایل kv
                screen_content = f'''{self.folder_name} = ObjectProperty(None)'''
                components_content = '''pass'''

                py = f'''
#start_import
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class {class_name}({"object" if inhrients else "Screen"}):
    #start_ObjectProperty
    {components_content if inhrients else screen_content} 
                '''
                py_file.write(py)



            if self.base_path == sc:
                WindowsManagerSetup(self.folder_name)
        except Exception as er:
            print(er)
nc = r"C:\Users\user\PycharmProjects\cinix\libs\components\notification_components"
s = ScreenFactory(r"C:\Users\user\PycharmProjects\MizdezhMarket\libs\screens", "shop")