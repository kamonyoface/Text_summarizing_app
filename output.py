from kivy.app import App
from kivy.lang import Builder


kv = Builder.load_string("""
BoxLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
    orientation: 'vertical'
    spacing: 300
    padding: 300

    Label:
        text: 'summarization of the text: bla bla bla bla bla'
    Button:
        text: 'Exit'
        on_release: app.stop()
""")


class OutPut(App):

    def build(self):
        return kv


if __name__ == "__main__":
    OutPut().run()
