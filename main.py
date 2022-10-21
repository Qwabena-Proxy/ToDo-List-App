import datetime
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


Window.size = (350,600)

class LayOut(GridLayout):
    pass

class Task_title(Widget):
    pass

class Task_description(Widget):
    pass

class Task_bar(Widget):
    pass

class Task_check(Widget):
    pass

class SHOWTODO(Widget):
    pass

class ADDTODO(Widget):
    pass

class ScreenOne(Screen):
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().strftime("%b"))
    day = str(datetime.datetime.now().strftime("%d"))
    day_name = datetime.datetime.now().strftime("%A")
    datee = f"[b]{day_name}, {day} {month} {year}[/b]"
    # pass

class ScreenTwo(Screen):
    pass

class WindowsScreenManager(ScreenManager):
    pass

class TODOLISTAPP(App):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('Main_screen.kv'))
        screen_manager.add_widget(Builder.load_file('Screen2.kv'))
        return screen_manager 

    def add_to_do(self):
        print("Called")
        screen_manager.get_screen("main").todo_list.add_widget(Task_title())
        screen_manager.get_screen("main").todo_list.add_widget(Task_description())
        screen_manager.get_screen("main").todo_list.add_widget(Task_bar())
        screen_manager.get_screen("main").todo_list.add_widget(Task_check())
    
    def complete(self, color, value, desc):
        if value == "down":
            color.background_color = 1 ,0 , .5, 1
            desc.text = f"[s]{desc.text}[/s]"
        else:
            remove = ["[s]","[/s]"]
            for i in remove:
                desc.text = desc.text.replace(i, "")
            color.background_color = 1 ,1 , 0, 1
        

if __name__ == '__main__':
    TODOLISTAPP().run()