from kivy.app import App
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
class Board(BoxLayout):
    puzzle = 
class Root(FloatLayout):
    board = ObjectProperty(None)
    def gotoTitle(self):
        self.clear_wigets()
        self.add_widget(Factory,Title())
    def gotoBoard(self,no):
        self.clear_wigets()
        self.board = Board(no)
        self.add_widget(self.board)
class MagicApp(App):
	title = "魔法陣パズル"
	def build(self):
		self.root.gotoTitle()
MagicApp().run()