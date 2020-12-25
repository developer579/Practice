from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Rotate
from kivy.uix.widget import Widget

class MyWidget(Widget):
    angle = 0
    step = 5
    def rotate(self, dt):
        self.canvas.clear()
        x = self.width * 0.3
        y = self.height * 0.3
        w = self.width * 0.4
        h = self.height * 0.4
        with self.canvas:
            Rotate(origin=(x+w/2,y+h/2), angle=self.angle)
            Color(1,0,0,1)
            Rectangle(pos=(x,y), size=(w,h))
        self.angle = self.angle+self.step
        if self.angle > 360:
            self.angle = self.angle-360
        if self.angle < -360:
            self.angle = self.angle+360
    def on_touch_down(self, touch): # omake
        self.step = -self.step
        
        

class rotateApp(App):
    def build(self):
        lbl = MyWidget()
        Clock.schedule_interval(lbl.rotate, 0.01)
        return lbl

rotateApp().run()
