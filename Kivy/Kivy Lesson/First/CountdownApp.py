from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class TextIN(TextInput):
    multiline = False
    time1 = 0
    def on_text_validate(self,*args):
        print(self.text)
        try:
            self.time1 = float(self.text)
        except:
            self.parent.parent.layout.lbl.text = "text is only value."
        else:
            print(self.time1)
            self.parent.parent.layout.lbl.time = self.time1
            self.parent.parent.layout.lbl.text = str(self.time1)
            self.parent.parent.layout.btn.text = "START"
            try:
                self.parent.parent.layout.btn.evt.cancel()
            except:
                print("evt is not ready.")
            else:
                pass

class MyLabel(Label):
    time = 0
class MyButton(Button):
    evt = None
    evt2 = None
    time2 = 0
    def on_press(self):
        if self.text == "START":
            if self.parent.parent.layout.txtI.time1 ==0:
                pass
            else:
                self.time2 = self.parent.parent.layout.lbl.time
                self.evt = Clock.schedule_interval(self.cb,0.1)
                print(self.parent.parent.layout.txtI.time1)
                self.text = "STOP"
        elif self.text == "RESTART":
            self.parent.parent.layout.lbl.time = self.time2
            self.parent.parent.layout.lbl.text = str(self.time2)
            self.evt()
            self.text = "STOP"
        else:
            self.evt.cancel()
            self.text = "START"
        
    def cb(self,dt):
        self.parent.parent.layout.lbl.time = round(self.parent.parent.layout.lbl.time - 0.1,1)
        self.parent.parent.layout.lbl.text = str(self.parent.parent.layout.lbl.time)
        if self.parent.parent.layout.lbl.time == 0:
            self.evt.cancel()
            self.text = "RESTART"
class MyRoot(BoxLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.layout = BoxLayout(orientation="vertical")
		self.layout.txtI = TextIN(text="0",size_hint_y=0.2,font_size=50)
		self.layout.lbl = MyLabel(text="-",font_size=100)
		self.layout.btn = MyButton(text="START",font_size=100)
		self.layout.add_widget(self.layout.txtI)
		self.layout.add_widget(self.layout.btn)
		self.layout.add_widget(self.layout.lbl)
		self.add_widget(self.layout)

class CountdownApp(App):
	def build(self):
		return MyRoot()
		
CountdownApp().run()