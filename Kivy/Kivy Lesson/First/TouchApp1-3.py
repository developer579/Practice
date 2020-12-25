from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

Label.font_size = 40

class ONOFFBUTTON(Button):
    def on_press(self):
        lbl = self.parent.parent.lbl
        btn = self.parent.parent.btn
        if btn.text == "ON":
            btn.text = "OFF"
            if lbl.text == "ON":
                lbl.text = "OFF"
        elif btn.text == "OFF":
            btn.text = "ON"
            if lbl.text == "OFF":
                lbl.text = "ON"
        else:
            btn.text = "OFF"
            lbl.text = "ON"
class MyRoot(BoxLayout):
    def __init__(self,**kwargs):
        super(MyRoot,self).__init__(**kwargs)
        box = BoxLayout(orientation="horizontal")
        self.lbl = Label(text="ON")
        self.btn = ONOFFBUTTON(text="ON")
        box.add_widget(self.lbl)
        box.add_widget(self.btn)
        self.add_widget(box)

class TouchApp(App):
    def build(self):
        return MyRoot()
        
TouchApp().run()
