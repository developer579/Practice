from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class FloatApp(App):
	def build(self):
		layout = FloatLayout()
		btn1 = Button(text="1st",size_hint=(0.2,0.2),right=400,y=50)
		btn2 = Button(text="2st",size_hint=(0.2,0.2),pos_hint={"center_x":0.5,"top":0.9})
		layout.add_widget(btn1)
		layout.add_widget(btn2)
		return layout
FloatApp().run()