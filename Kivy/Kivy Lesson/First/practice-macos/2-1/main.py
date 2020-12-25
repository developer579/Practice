from kivy.app import App
from kivy.uix.button import Button

class MyButton(Button):
    def on_press(self):
        if self.text=='OFF':
            self.text = 'ON'
        else:
            self.text = 'OFF'

class MyApp(App):
    def build(self):
        return MyButton(text='OFF')

MyApp().run()
