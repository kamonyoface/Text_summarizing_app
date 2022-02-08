from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (1400, 700)

class MainScreen(Screen):
    pass

class OutputScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class SavedScreen(Screen):
    pass

class landing_page(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(OutputScreen(name='output'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(SavedScreen(name='saved'))

        return sm

if __name__ == "__main__":
    window = landing_page()
    window.run()
