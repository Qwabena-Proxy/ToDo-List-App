import datetime
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

Window.size = (350,600)

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

if __name__ == '__main__':
    TODOLISTAPP().run()