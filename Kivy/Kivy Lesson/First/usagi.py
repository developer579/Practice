from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label

class MyLabel(Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        evt = Clock.schedule_interval(self.cb,1)
    def cb(self,*args):
        print("うさぎ")
        self.text += " USAGI"

class UsagiApp(App):
    def build(self):
        return MyLabel(text="USAGI",font_size=100,bold=True)

UsagiApp().run()