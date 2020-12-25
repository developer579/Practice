from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyButton(Button):
    def on_press(self):
        self.size_hint_x += 0.1

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        b1 = MyButton(text='1')
        b2 = MyButton(text='2')
        layout.add_widget(b1)
        layout.add_widget(b2)
        return layout

MyApp().run()
        
        
