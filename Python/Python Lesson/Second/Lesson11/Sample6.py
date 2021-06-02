import urllib.request as ur

page = ur.urlopen("https://www.python.org/")

html = page.read()
str = html.decode()

print(str)