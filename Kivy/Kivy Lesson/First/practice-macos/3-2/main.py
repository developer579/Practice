from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class SlotLabel(Label):
    value = NumericProperty(0)
    font_size = 48
    evt = None
    def on_value(self, *args):
        self.text = str(self.value)
    def change_value(self, dt):
        self.value = random.randint(0,9)

class SlotButton(Button):
    counter = 0
    font_size = 28
    def on_press(self):
        upper_box = self.parent.children[1]
        t = self.counter%5
        if t == 0:
            for lbl in upper_box.children:
                lbl.evt = Clock.schedule_interval(lbl.change_value, 0.05)
            self.text = 'Stop'
        elif t == 4:
            for lbl in upper_box.children:
                lbl.value = 0
            self.text = 'Start'
        else:
            lbl = upper_box.children[3-t]
            lbl.evt.cancel()
            if t == 3:
                self.text = 'Reset'
        self.counter += 1

class SlotApp(App):
    def build(self):
        root_box = BoxLayout(orientation='vertical')
        upper_box = BoxLayout(size_hint_y=9)
        for i in range(3):
            upper_box.add_widget(SlotLabel(text='0'))
        root_box.add_widget(upper_box)
        root_box.add_widget(SlotButton(text='Start'))
        return root_box

SlotApp().run()
