from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
import random


Window.size = (1400, 700)

class Display(BoxLayout):
    pass

class MainScreen(Screen):
    pass

class OutputScreen(Screen):
    import pyperclip as pc
    import random
    red = [1, 0, 0, 1]
    green = [0, 1, 0, 1]
    blue = [0, 0, 1, 1]
    purple = [1, 0, 1, 1]
    colors = [red, green, blue, purple]
    pass

class FilesScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class landing_page(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return Display()


if __name__ == "__main__":
    window = landing_page()
    window.run()
