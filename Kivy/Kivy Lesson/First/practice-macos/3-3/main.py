from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class TimerTextInput(TextInput):
    input_filter = 'int'
    multiline = False
    def on_text(self, *args):
        lbl = self.parent.children[0]
        try:
            lbl.value = int(self.text)
        except ValueError:
            lbl.value = 0

class TimerButton(Button):
    font_size = 48
    def on_press(self):
        lbl = self.parent.children[0]
        if lbl.value > 0:
            ti = self.parent.children[2]
            ti.disabled = True
            self.disabled = True
            lbl.evt = Clock.schedule_interval(lbl.timer, 1)

class TimerLabel(Label):
    evt = None
    font_size = 48
    value = NumericProperty(0)
    def on_value(self, *args):
        self.text = str(self.value)
    def timer(self, dt):
        self.value -= 1
        if self.value == 0:
            self.evt.cancel()
            ti = self.parent.children[2]
            ti.disabled = False
            ti.on_text()
            btn = self.parent.children[1]
            btn.disabled = False


class TimerApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(TimerTextInput(font_size=32))
        box.add_widget(TimerButton(text='Start', size_hint_y=5))
        box.add_widget(TimerLabel(text='-', size_hint_y=5))
        return box

TimerApp().run()
