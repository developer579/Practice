from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LeftButton(Button):
    def on_press(self):
        self.parent.parent.left_press()

class RightButton(Button):
    def on_press(self):
        self.parent.parent.right_press()

        
class MyRoot(BoxLayout):
    orientation='vertical'
    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)
        self.upper = BoxLayout(orientation='horizontal',size_hint_y=0.2)
        self.upper.add_widget(LeftButton(text='Left'))
        self.upper.add_widget(RightButton(text='Right'))
        self.add_widget(self.upper)
        self.lower = BoxLayout()
        self.add_widget(self.lower)
        self.left_press()

    def left_press(self):
        self.lower.clear_widgets()
        self.lower.orientation='horizontal'
        self.lower.add_widget(Label(text='A'))
        self.lower.add_widget(Button(text='B'))
        self.lower.add_widget(Label(text='C'))
        
    def right_press(self):
        self.lower.clear_widgets()
        self.lower.orientation='vertical'
        self.lower.add_widget(Label(text='D'))
        self.lower.add_widget(Button(text='E'))
        self.lower.add_widget(Label(text='F'))
        self.lower.add_widget(Button(text='G'))

    
class SwitchScreenApp(App):
    def build(self):
        return MyRoot()
    
SwitchScreenApp().run()

    
