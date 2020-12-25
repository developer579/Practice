from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label

class ColoredLabel(Label):
    counter = 0
    def __init__(self, **kwargs):
        super(ColoredLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.change, 0.5)
    def change(self, dt):
        self.counter += 1
        if self.counter%4==0:
            self.color = (1,1,1,1) # white
        elif self.counter%4==1:
            self.color = (1,0,0,1) # red
        elif self.counter%4==2:
            self.color = (0,1,0,1) # green
        else:
            self.color = (0,0,1,1) # blue

class ColoredLabelApp(App):
    def build(self):
        return ColoredLabel(text='Hello, world.', font_size=24)

ColoredLabelApp().run()
