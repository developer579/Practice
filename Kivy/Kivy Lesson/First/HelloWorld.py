from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    title = "My 1st App"
    def build(self):
        return Button(text="Hello,world.")

MyApp().run()