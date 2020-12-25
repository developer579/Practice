from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("H2B1-1.kv")

class MyButton(Button):
	pass

class MyApp(App):
	def build(self):
		layout = BoxLayout()
		btn1 = Button(text="Button1")
		btn2 = MyButton(text="Button2")
		layout.add_widget(btn1)
		layout.add_widget(btn2)
		return layout

MyApp().run()