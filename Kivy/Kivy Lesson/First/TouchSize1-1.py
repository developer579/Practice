from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class ButtonA(Button):
    def on_press(self):
        btn = self.parent.parent.btn1
        btn.size_hint_x = btn.size_hint_x * 1.02
        btn.size_hint_y = btn.size_hint_y * 1.02

class ButtonB(Button):
    def on_press(self):
        btn = self.parent.parent.btn2
        btn.size_hint_x = btn.size_hint_x * 1.02
        btn.size_hint_y = btn.size_hint_y * 1.02

class MyRoot(FloatLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		layout = FloatLayout()
		self.btn1 = ButtonA(text="",size_hint_x=0.2,size_hint_y=0.2,pos_hint={"center_x":0.3,"center_y":0.5})
		self.btn2 = ButtonB(text="",size_hint_x=0.2,size_hint_y=0.2,pos_hint={"center_x":0.7,"center_y":0.5})
		layout.add_widget(self.btn1)
		layout.add_widget(self.btn2)
		self.add_widget(layout)

class TouchSize(App):
	def build(self):
		return MyRoot()

TouchSize().run()