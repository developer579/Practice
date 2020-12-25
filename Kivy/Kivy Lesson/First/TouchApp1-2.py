from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

Label.font_size = 32

class IncreaseButton(Button):
	def on_press(self):
		lbl = self.parent.parent.lbl
        if lbl.text is "ON":
            lbl.text = "OFF"
        else:
            lbl.text = "ON"
class ResetButton(Button):
	def on_press(self):
		lbl = self.parent.parent.lbl
class MyRoot(BoxLayout):
	orientation = "horizontal"
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.lbl = Label(text="ON")
		self.add_widget(self.lbl)
		box = BoxLayout(orientation="vertical")
		btn1 = IncreaseButton(text="Increase")
		btn2 = ResetButton(text="Reset")
		box.add_widget(btn1)
		box.add_widget(btn2)
		self.add_widget(box)
class counterApp(App):
	def build(self):
		return MyRoot()
counterApp().run()