from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

Albl = Label(text="A")
Bbtn = Button(text="B")
Clbl = Label(text="C")
Dlbl = Label(text="D")
Ebtn = Button(text="E")
Flbl = Label(text="F")
Gbtn = Button(text="G")

ABClist = [Albl,Bbtn,Clbl]
DEFGlist = [Dlbl,Ebtn,Flbl,Gbtn]

class PressLeft(Button):
    def on_press(self):
        box2 = self.parent.parent.box2
        box2.clear_widgets()
        
        box2.orientation = "horizontal"
        #Albl = Label(text="A")
        #Bbtn = Button(text="B")
        #Clbl = Label(text="C")
        
        for i in ABClist:
            box2.add_widget(i)

class PressRight(Button):
    def on_press(self):
        box2 = self.parent.parent.box2
        box2.clear_widgets()
        
        box2.orientation = "vertical"
        
        for i in DEFGlist:
            box2.add_widget(i)     
        
class MyRoot(BoxLayout):
    orientation = "vertical"
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        box1 = BoxLayout(orientation="horizontal",size_hint_y=0.2)
        Lbtn = PressLeft(text="Left")
        Rbtn = PressRight(text="Right")
        box1.add_widget(Lbtn)
        box1.add_widget(Rbtn)
        self.add_widget(box1)

        self.box2 = BoxLayout(orientation="horizontal")

        #Albl = Label(text="A")
        #Bbtn = Button(text="B")
        #Clbl = Label(text="C")
        #Dlbl = Label(text="D")
        #Ebtn = Button(text="E")
        #Flbl = Label(text="F")
        #Gbtn = Button(text="G")
            
        for i in ABClist:
            self.box2.add_widget(i)
        self.add_widget(self.box2)

class SwitchScreen(App):
	def build(self):
		return MyRoot()

SwitchScreen().run()