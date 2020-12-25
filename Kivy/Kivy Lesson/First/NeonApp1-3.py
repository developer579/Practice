from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class MyLabel(Label):
    Re = NumericProperty(0)
    Gr = NumericProperty(0)
    Bu = NumericProperty(0)
    time = NumericProperty(0)
    def on_time(self,*args):
        self.color = (self.Re,self.Gr,self.Bu,1)

class MyButton(Button):
    evt = None
    
    def on_press(self,*args):
        if self.text == "ACTIVATE":
            self.evt = Clock.schedule_interval(self.cb,0.05)
            self.text = "DEACTIVATE"
        else:
            self.evt.cancel()
            self.text = "ACTIVATE"
            self.parent.lbl.color = (0,0,0,0)
            self.parent.lbl.Re = 0
            self.parent.lbl.Gr = 0
            self.parent.lbl.Bu = 0
            
    def cb(self,dt):
        self.parent.lbl.time = self.parent.lbl.time + 0.1
        
        if self.parent.lbl.Re > 1:
            self.parent.lbl.Re = self.parent.lbl.Re + 0.02
        else:
            self.parent.lbl.Re = self.parent.lbl.Re - 0.08
                
        if self.parent.lbl.Gr > 1:
            self.parent.lbl.Gr = self.parent.lbl.Gr + 0.04
        else:
            self.parent.lbl.Gr = self.parent.lbl.Gr - 0.04
            
        if self.parent.lbl.Bu > 1:
            self.parent.lbl.Bu = self.parent.lbl.Bu + 0.08
        else:
            self.parent.lbl.Bu = self.parent.lbl.Bu - 0.02

class NeonApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        layout.lbl = MyLabel(text="Hello world.",color=(0,0,0,0),font_size=200)
        layout.btn = MyButton(text="ACTIVATE",color=(1,1,1,1),size_hint_y=0.2,font_size=60)
        layout.add_widget(layout.lbl)
        layout.add_widget(layout.btn)
        return layout
NeonApp().run()