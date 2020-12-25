from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class LabelA(Label):
    counter = 0
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.evt = Clock.schedule_interval(self.slot,0.05)
    def slot(self,dt):
        self.counter += 1
        if self.counter %9==0:
            self.text = str(1)
        elif self.counter %9==1:
            self.text = str(2)
        elif self.counter %9==2:
            self.text = str(3)
        elif self.counter %9==3:
            self.text = str(4)
        elif self.counter %9==4:
            self.text = str(5)
        elif self.counter %9==5:
            self.text = str(6)
        elif self.counter %9==6:
            self.text = str(7)
        elif self.counter %9==7:
            self.text = str(8)
        else:
            self.text = str(9)
            
        if self.text == str(7):
            self.color = (1,0,0,1)
        else:
            self.color = (1,1,1,1)
class LabelB(Label):
    counter = 4
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.evt = Clock.schedule_interval(self.slot,0.05)
    def slot(self,dt):
        self.counter += 1
        if self.counter %9==0:
            self.text = str(1)
        elif self.counter %9==1:
            self.text = str(2)
        elif self.counter %9==2:
            self.text = str(3)
        elif self.counter %9==3:
            self.text = str(4)
        elif self.counter %9==4:
            self.text = str(5)
        elif self.counter %9==5:
            self.text = str(6)
        elif self.counter %9==6:
            self.text = str(7)
        elif self.counter %9==7:
            self.text = str(8)
        else:
            self.text = str(9)
            
        if self.text == str(7):
            self.color = (1,0,0,1)
        else:
            self.color = (1,1,1,1)
class LabelC(Label):
    counter = 8
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.evt = Clock.schedule_interval(self.slot,0.05)
    def slot(self,dt):
        self.counter += 1
        if self.counter %9==0:
            self.text = str(1)
        elif self.counter %9==1:
            self.text = str(2)
        elif self.counter %9==2:
            self.text = str(3)
        elif self.counter %9==3:
            self.text = str(4)
        elif self.counter %9==4:
            self.text = str(5)
        elif self.counter %9==5:
            self.text = str(6)
        elif self.counter %9==6:
            self.text = str(7)
        elif self.counter %9==7:
            self.text = str(8)
        else:
            self.text = str(9)
            
        if self.text == str(7):
            self.color = (1,0,0,1)
        else:
            self.color = (1,1,1,1)
class StopButton(Button):
    counter = 0
    def on_press(self):
        if self.counter == 0:
            self.parent.layout.lblA.evt.cancel()
            self.counter += 1
        elif self.counter == 1:
            self.parent.layout.lblB.evt.cancel()
            self.counter += 1
        elif self.counter == 2:
            self.parent.layout.lblC.evt.cancel()
            self.counter += 1
            self.text = "RESTART"
        else:
            self.parent.layout.lblA.evt()
            self.parent.layout.lblB.evt()
            self.parent.layout.lblC.evt()
            self.counter = 0
            self.text = "STOP"
            
class MyRoot(BoxLayout):
    orientation = "vertical"
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="horizontal")
        self.layout.lblA = LabelA(text="1",font_size=300,bold=True)
        self.layout.lblB = LabelB(text="5",font_size=300,bold=True)
        self.layout.lblC = LabelC(text="9",font_size=300,bold=True)
        self.layout.add_widget(self.layout.lblA)
        self.layout.add_widget(self.layout.lblB)
        self.layout.add_widget(self.layout.lblC)
        StopBt = StopButton(text="STOP",size_hint_y=0.2,font_size=50)
        self.add_widget(self.layout)
        self.add_widget(StopBt)
        
class SlotApp(App):
    def build(self):
        return MyRoot()

SlotApp().run()