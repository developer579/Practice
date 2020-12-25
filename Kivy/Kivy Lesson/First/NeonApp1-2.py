from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty

Label.font_size = 100

evt = None
Re = NumericProperty(0)
Gr = NumericProperty(0)
Bu = NumericProperty(0)

time = NumericProperty(0)

class MyLabel(Label):
    
    def on_time(self,*args):
        self.color = (Re,Gr,Bu,1)

class NeonApp(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout()
        layout.lbl = MyLabel(text="Hello world.")
        layout.add_widget(layout.lbl)
        self.add_widget(layout)

def cb(dt):
           
    if Re > 1:
        Re = Re + 0.02
    else:
        Re = Re - 0.08
                
    if Gr > 1:
        Gr = Gr + 0.04
    else:
        Gr = Gr - 0.04
            
    if Bu > 1:
        Bu = Bu + 0.08
    else:
        Bu = Bu - 0.02

evt = Clock.schedule_interval(cb,0.05)

class NeonAPP2(App):
    def build(self):
        return NeonApp()

NeonAPP2().run()