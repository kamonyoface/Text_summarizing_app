from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty

from summarizer import *

model_name = 'summarizing_model'


class AppLayout(BoxLayout):
    text_input = ObjectProperty()
    text_to_sum = StringProperty("")

    def summarize(self, text):
        summary = generate_summary(text, 200, 100, model_name)
        output = summary.summarize()
        return output
    
    def submit(self):
        self.text_to_sum = self.text_input.text
        out = self.summarize(self.text_to_sum)
        self.output_window.text = out
        print('ready')
        


class Frontend(App):
    def build(self):
        return AppLayout()


if __name__ == "__main__":
    window = Frontend()
    window.run()