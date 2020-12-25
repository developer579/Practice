from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyTextInput(TextInput):
        def on_text_validate(self):
                self.parent.lbl.text = self.text

class MyButton(Button):
        counter = 0
        def on_press(self):
                self.counter += 1
                if self.counter%3 == 0:
                        self.parent.lbl.color = (1,1,1,1)
                elif self.counter%3 == 1:
                        self.parent.lbl.color = (0,0,1,1)
                else:
                        self.parent.lbl.color = (1,0,0,1)
        
class ChangeTextColorApp(App):
	def build(self):
                root = BoxLayout(orientation='vertical')
                ti = MyTextInput(multiline=False)
                root.lbl = Label(text='')
                btn = MyButton(text='Change the text color')
                root.add_widget(ti)
                root.add_widget(root.lbl)
                root.add_widget(btn)
                return root

ChangeTextColorApp().run()


