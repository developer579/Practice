import requests
from bs4 import BeautifulSoup

# Webページを分析して解析する
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

# title、h2、liのタグを検索して、その文字列を表示する
print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)