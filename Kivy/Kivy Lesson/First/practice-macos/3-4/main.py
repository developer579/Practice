from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyFloatLayout(FloatLayout):
    counter = 1
    def on_touch_down(self, touch):
        btn = Button(pos=touch.pos, text=str(self.counter),\
                         size_hint=(0.05,0.05))
        self.add_widget(btn)
        self.counter += 1   

class touch_and_generateApp(App):
    def build(self):
        return MyFloatLayout()

touch_and_generateApp().run()
