from kivy.app import App
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

def my_on_touch_down(*args):
	print("You touched the window.")
Window.bind(on_touch_down=my_on_touch_down)

class MyWidget(Widget):
	no = NumericProperty(0)
	def on_touch_down(self,touch):
		if self.collide_point(*touch.pos):
			print("You touched the widget"+str(self.no)+".")
		return super().on_touch_down(touch)

class MyBoxLayout(MyWidget,BoxLayout):
	pass
class MyButton(MyWidget,Button):
	pass
class MyLabel(MyWidget,Label):
	pass

class TouchEventTestApp(App):
    def build(self):
        root = MyBoxLayout(no=1,orientation="horizontal")
        w2 = MyBoxLayout(no=2,orientation="vertical")
        w3 = MyLabel(no=3,text="3")
        w4 = MyButton(no=4,text="4")
        w5 = MyBoxLayout(no=5)
        w6 = MyLabel(no=6,text="6")
        w7 = MyButton(no=7,text="7")
        w8 = MyBoxLayout(no=8,orientation="vertical")
        w9 = MyLabel(no=9,text="9")
        list1 = [w3,w4,w5]
        list2 = [w6,w7]
        list3 = [w2,w8]
        for i in list2:
            w5.add_widget(i)
        for i in list1:
            w2.add_widget(i)
        w8.add_widget(w9)
        for i in list3:
            root.add_widget(i)
        return root

TouchEventTestApp().run()