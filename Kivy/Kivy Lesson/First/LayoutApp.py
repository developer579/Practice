from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class LayoutApp(App):
	title = "LayoutApp"
	def build(self):
		layout = BoxLayout(orientation="horizontal")
		b1 = Button(text="1st")
		b2 = Button(text="2nd")
		b3 = Button(text="3rd")
		layout.add_widget(b1)
		layout.add_widget(b2)
		layout.add_widget(b3)
		return layout
        
LayoutApp().run()