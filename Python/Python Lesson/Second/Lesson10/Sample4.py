import json

j = open("Sample.json","r")

data = json.load(j)

print(data)

j.close()