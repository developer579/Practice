from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class RemoveA(Button):
	def on_press(self):
		btn = self.parent.parent.b1
		layout = self.parent.parent.layout
		layout.remove_widget(btn)

class RemoveB(Button):
	def on_press(self):
		btn = self.parent.parent.b2
		layout = self.parent.parent.layout
		layout.remove_widget(btn)

class RemoveC(Button):
	def on_press(self):
		btn = self.parent.parent.b3
		layout = self.parent.parent.layout
		layout.remove_widget(btn)
		
class SizeHintApp(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="horizontal")
        self.b1 = RemoveA(text="1st",size_hint_x=1)
        self.b2 = RemoveB(text="2nd",size_hint_x=3)
        self.b3 = RemoveC(text="3rd",size_hint=[2,0.5])
        self.layout.add_widget(self.b1)
        self.layout.add_widget(self.b2)
        self.layout.add_widget(self.b3)
        self.add_widget(self.layout)
		
class ButtonRemove(App):
    def build(self):
        return SizeHintApp()
    
ButtonRemove().run()