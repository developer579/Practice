from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyButton(Button):
        def on_press(self):
                self.parent.remove_widget(self)

class MyApp(App):
	def build(self):
                layout = BoxLayout(orientation='horizontal')
                b1 = MyButton(text='1st')
                b2 = MyButton(text='2nd')
                b3 = MyButton(text='3rd')
                layout.add_widget(b1)
                layout.add_widget(b2)
                layout.add_widget(b3)
                return layout

MyApp().run()


