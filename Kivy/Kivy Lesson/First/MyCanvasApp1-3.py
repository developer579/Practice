from kivy.app import App
from kivy.graphics import Color,Ellipse
from kivy.uix.label import Label

class MyLabel(Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update)
        self.bind(size=self.update)
        self.update()
    def update(self,*args):
        self.canvas.clear()
        with self.canvas:
            Color(1,0,0,1)
            Ellipse(pos=self.pos,size=self.size)

class MyCanvasApp(App):
	def build(self):
		return MyLabel(text="Hello,canvas.")

MyCanvasApp().run()