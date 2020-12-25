from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock 
from kivy.graphics import Color,Rectangle,Rotate
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = 250,250

class MyCanvas(Label):
    counter=0
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update)
        self.bind(size=self.update)
        self.update()
        evt = Clock.schedule_interval(self.cb,0.01)
    def update(self,*args):
        self.canvas.add(Color(1,1,1,1))
        self.canvas.add(Rectangle(pos=[100,100],size=[300,300]))
    def cb(self,*args):
        self.canvas.clear()
        if self.counter >=0:
            self.counter += 10
        else:
            self.counter += -10
        self.canvas.add(Rotate(origin=[250,250],angle=self.counter))
        self.update()
        print(str(self.counter))
    def on_touch_down(self,touch):
        self.counter = -self.counter
class CanvasLesson2App(App):
    def build(self):
        return MyCanvas()

CanvasLesson2App().run()