import urllib.request

page = urllib.request.urlopen("http://www.python.org/")

html = page.read()
str = html.decode()

print(str)