from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SizeHintApp(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal")
        btn1 = Button(text="1st",size_hint_x=1) 
        btn2 = Button(text="2nd",size_hint_x=3)
        btn3 = Button(text="3rd",size_hint=[2,0.5])
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout

SizeHintApp().run()