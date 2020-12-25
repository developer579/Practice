from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from random import randint

class Ball(Widget):
    r = 25
    dx = 0
    dy = 0
    ball_color = (1,1,1,1)
    def __init__(self, **kwargs):
        super(Ball, self).__init__()
        self.size_hint = (None, None)
        self.size = (2*self.r, 2*self.r)
        self.pos = (randint(0,Window.width-2*self.r), randint(0,Window.height-2*self.r))
        self.dx = randint(-10,10)
        self.dy = randint(-10,10)
        self.ball_color = kwargs['ball_color']
        with self.canvas:
            Color(*self.ball_color)
            Ellipse(pos=self.pos, size=self.size)
    def move(self, dt):
        self.x += self.dx
        self.y += self.dy
        self.canvas.clear()
        with self.canvas:
            Color(*self.ball_color)
            Ellipse(pos=self.pos, size=self.size)
        if self.x <= 0 or self.right >= Window.width:
            self.dx = -self.dx
        if self.y <= 0 or self.top >= Window.height:
            self.dy = -self.dy

class bounceApp(App):
    def build(self):
        layout = FloatLayout()
        red = Ball(ball_color=(1,0,0,1))
        green = Ball(ball_color=(0,1,0,1))
        blue = Ball(ball_color=(0,0,1,1))
        layout.add_widget(red)
        layout.add_widget(green)
        layout.add_widget(blue)
        Clock.schedule_interval(red.move, 0.01)
        Clock.schedule_interval(green.move, 0.02)
        Clock.schedule_interval(blue.move, 0.03)
        return layout

bounceApp().run()
