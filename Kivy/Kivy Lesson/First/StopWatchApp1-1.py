from kivy.app import App
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyLabel(Label):
	time = NumericProperty(0)
	def on_time(self,*args):
		self.text = str(self.time)

class MyButton(Button):
	evt = None
	def on_press(self):
		if self.text == "start":
			self.evt = Clock.schedule_interval(self.cd,0.2)
			self.text = "stop"
		else:
			self.evt.cancel()
			self.text = "start"
	def cd(self,dt):
		self.parent.lbl.time = round(self.parent.lbl.time+0.2,2)

class StopWatchApp(App):
	def build(self):
		layout = BoxLayout(orientation="horizontal")
		layout.lbl = MyLabel(text="0")
		layout.btn = MyButton(text="start")
		layout.add_widget(layout.lbl)
		layout.add_widget(layout.btn)
		return layout

StopWatchApp().run()