from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
import random
import pyperclip as pc

from summarizer import *
from scraper import *

model_path = 'summarizing_model' # specify model path

summarizing_model = sum_model(model_path) # initialize summarizer object
summarizing_model.initialize_model() # initialize model and tokenizer inside the object

Window.size = (1400, 700)


class Display(BoxLayout):
    pass

class MainScreen(Screen):
    text_type = 'text'

    def summarize(self, text): # define function for generating summaries

        if self.text_type == "text":
            pass
        elif self.text_type == 'URL':
            try:
                article = scrape_article(text)
                article.scrape_data()
                text = article.data.text
            except:
                text = 'Count not scrape the website'
                print('could not scrape the website')
        else:
            # popup window for reminding about choosing the text file
            pass

        if text == 'Cound not scrape the website':
            output = text
        else:
            try:
                output = summarizing_model.summarize(text) # use previously initialized model to generate summary
            except RuntimeError:
                output = 'Input is too short to summarize'
        return output

    def submit(self):
        text = str(self.text_input.text)
        self.out = self.summarize(text)
        print(f'generated summary: {self.out}')

    def toggle(self, x):
        self.text_type = x
        print(f'Chosen text type: {x}')

class OutputScreen(Screen):
    red = [1, 0, 0, 1]
    green = [0, 1, 0, 1]
    blue = [0, 0, 1, 1]
    purple = [1, 0, 1, 1]
    colors = [red, green, blue, purple]
    choice = random.choice(colors)

    def copy_output(self):
        copied_output_text = self.ids.output_text.text
        pc.copy(copied_output_text)
    def save(self):
        try:
            with open('saved_summaries/'+self.manager.get_screen('MainScreen').ids.title.text+'.txt', 'w') as f:
                f.write(self.ids.output_text.text)
        except:
            print('Title not provided!')

    def output(self, button_instance):
        self.manager.current = 'SavedOutput'

    def output_presented(self):
        self.new_output_saved =  str(self.ids.output_text.text)


class FilesScreen(Screen):
    def output(self):
        self.manager.current = 'SavedOutput'


class AboutScreen(Screen):
    pass

class SavedOutput(Screen):
    def copy_output(self):
        copied_output_text = self.ids.saved_output_text.text
        pc.copy(copied_output_text)

    


class landing_page(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return Display()


if __name__ == "__main__":
    window = landing_page()
    window.run()
