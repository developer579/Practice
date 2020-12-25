from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyTI(TextInput):
	multiline = False
	def on_text_validate(self):
		print(self.text)
		lbl = self.parent.parent.lbl
		lbl.text = self.text

class Color(Button):
    def on_press(self):
        lbl = self.parent.parent.lbl
        if str(lbl.color) == str([1,1,1,1]):
            lbl.color = (0,0,1,1)
        elif str(lbl.color) == str([0,0,1,1]):
            lbl.color = (1,0,0,1)
        elif str(lbl.color) == str([1,0,0,1]):
            lbl.color = (1,1,1,1)
        else:
            lbl.text = str(lbl.color)
        
        
class MyRoot(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical")
        tex = MyTI(text="Please Enter")
        self.lbl = Label(text="",color=[1,1,1,1])
        btn = Color(text="Change the text color")
        box.add_widget(tex)
        box.add_widget(self.lbl)
        box.add_widget(btn)
        self.add_widget(box)

class Textmaker(App):
	def build(self):
		return MyRoot()

Textmaker().run()
		