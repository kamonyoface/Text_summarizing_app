from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty

from summarizer import * # Import the summarizing module (needs a 'summarizer.py' file to be in the same directory)

model_path = 'summarizing_model' # specify model path

summarizing_model = sum_model(model_path) # initialize summarizer object
summarizing_model.initialize_model() # initialize model and tokenizer inside the object


class AppLayout(BoxLayout):
    text_input = ObjectProperty()
    text_to_sum = StringProperty("")

    def summarize(self, text): # define function for generating summaries
        output = summarizing_model.summarize(text) # use previously initialized model to generate summary
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