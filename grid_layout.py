from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionBar
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
Window.size = (1200, 700)
Window.clearcolor = (1, 1, 1, 1)

class MyGridLayout(GridLayout):
    pass

class Grid_LayoutApp(App):
    def build(self):


        landing = BoxLayout(orientation='vertical' ,spacing=10, padding=10)
        landing.size_hint = (0.9, 0.9)
        landing.pos_hint = {"center_x":0.5,"center_y":0.5}



        landing.heading = GridLayout(cols = 3, spacing=10, padding=50)
        landing.heading.size_hint = (0.9, 1)
        landing.heading.pos_hint = {"center_x":0.5,"center_y":0.5}

        landing.heading.lbl = Label(text ='Summarizing text app', font_size=100, bold=True, halign="left", color= (0, 0, 0, 0.5))
        landing.heading.add_widget(landing.heading.lbl)
        landing.heading.empty = Label(text ='')

        landing.heading.add_widget(landing.heading.empty)
        landing.heading.empty2 = Label(text ='')

        landing.heading.add_widget(landing.heading.empty2)
        landing.add_widget(landing.heading)


        landing.descryption = GridLayout(cols = 3, spacing=10, padding=50)
        landing.descryption.size_hint = (2, 1)
        landing.descryption.pos_hint = {"center_x":0.5,"center_y":0.5}
        landing.descryption.lbl = Label(text ='Provide text', italic=True, color= (0, 0, 0, 0.5), font_size=40)
        landing.descryption.add_widget(landing.descryption.lbl)
        landing.descryption.empty = Label(text ='')
        landing.descryption.empty.size_hint = (0.44, 1)
        landing.descryption.empty.pos_hint = {"center_x":0.5,"center_y":0.5}

        landing.descryption.add_widget(landing.descryption.empty)
        landing.descryption.empty2 = Label(text ='')
        landing.descryption.empty2.size_hint = (0.44, 1)
        landing.descryption.empty2.pos_hint = {"center_x":0.5,"center_y":0.5}

        landing.descryption.add_widget(landing.descryption.empty2)
        landing.add_widget(landing.descryption)



        landing.user_input = TextInput(text ='This is input', multiline=False, background_color= (236/255, 236/255, 236/255, 1), background_normal='')
        landing.user_input.pos_hint = {"center_x":0.5,"center_y":0.5}
        landing.user_input.size_hint = (0.9, 1)
        landing.add_widget(landing.user_input)



        landing.button = GridLayout(cols = 3, spacing=10, padding=50)
        landing.button.size_hint = (0.4, 1)
        landing.button.pos_hint = {"center_x":0.5,"center_y":0.5}

        landing.button.summarize = Button(text ='Summarize', font_size=40, bold=True, background_color= (56/255, 125/255, 240/255, 1), background_normal='')
        landing.button.summarize.size_hint = (0.4, 1)
        landing.button.summarize.pos_hint = {"center_x":0.5,"center_y":0.5}
        landing.button.add_widget(landing.button.summarize)

        landing.button.lbl = Label(text ='')
        landing.button.lbl.size_hint = (0.1, 1)
        landing.button.lbl.pos_hint = {"center_x":0.5,"center_y":0.5}
        landing.button.add_widget(landing.button.lbl)

        landing.button.cancel = Button(text ='Cancel', font_size=40, bold=True, background_color= (56/255, 125/255, 240/255, 1), background_normal='')
        landing.button.cancel.size_hint = (0.4, 1)
        landing.button.cancel.pos_hint = {"center_x":0.5,"center_y":0.5}
        landing.button.add_widget(landing.button.cancel)
        landing.add_widget(landing.button)



        landing.output = Label(text ='This is output', color= (0, 0, 0, 0.5))
        landing.add_widget(landing.output)



        landing.save = GridLayout(cols = 3, spacing=10, padding=50)
        landing.save.size_hint = (1, 1)
        landing.save.pos_hint = {"center_x":0.5,"center_y":0.5}

        landing.save.save_btn = Button(text ='Save', font_size=40, bold=True, background_color= (56/255, 125/255, 240/255, 1), background_normal='')
        landing.save.save_btn.size_hint = (0.4, 1)
        landing.save.save_btn.pos_hint = {"center_x":0.5,"center_y":0.5}

        landing.save.save_lbl = Label(text ='')
        landing.save.save_lbl2 = Label(text ='')
        landing.save.add_widget(landing.save.save_btn)
        landing.save.add_widget(landing.save.save_lbl)
        landing.save.add_widget(landing.save.save_lbl2)
        landing.add_widget(landing.save)




        return landing


root = Grid_LayoutApp()

root.run()
