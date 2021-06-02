import urllib.request
from html.parser import HTMLParser

class SampleHTMLParser(HTMLParser):
	def __init__(self):
		HTMLPaeser.__init__(self)
		self.title = False
	def handle_starttag(self,tag,attr):
		if tag == "title":
			self.title = True
	def handle_data(self,data):
		if self.title = True:
			print("タイトル：",data)
			self.title = False

page = urllib.request.urlopen("https://www.python.org/")

html = page.read()
str = html.decode()

p = SampleHTMLParser()
p.feed(str)

p.close()