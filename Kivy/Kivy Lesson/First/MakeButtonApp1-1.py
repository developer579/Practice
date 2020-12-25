from kivy.app import App
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

def my_on_touch_down(*args):
	print("You touched the window.")
Window.bind(on_touch_down=my_on_touch_down)

class MyWidget(Widget):
    no = NumericProperty(0)
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            print("You touched the point",touch.pos,".")
            btn = Button(size_hint=(0.2,0.2),pos=touch.pos)
            self.layout.add_widget(btn)
        return super().on_touch_down(touch)

class MyLayout(MyWidget,FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
class MyApp(App):
    def build(self):
        return MyLayout()

MyApp().run()

