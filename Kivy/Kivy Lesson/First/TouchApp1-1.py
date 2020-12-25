from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

Label.font_size = 40

class ONOFF(Button):
    def on_press(self):
        lbl = self.lbl
        if lbl.text == "ON":
            lbl.text = "OFF"
        else:
            lbl.text = "ON"

class MyRoot(BoxLayout):
    orientation = "horizontal"
    def build(self):
        self.lbl = Label(text="ON")
        btn = Button(text=self.lbl.text)
class TouchONOFF(App):
    def build(self):
        return MyRoot()
TouchONOFF().run()