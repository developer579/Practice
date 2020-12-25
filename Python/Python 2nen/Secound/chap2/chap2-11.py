import requests

image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

filename = image_url.split("/")[-1]

with open(filename, mode="wb") as f:
    f.write(imgdata.content)