import json

f = open("Sample0.json","w")

json.dump({"東京":30,"大阪":20},f)

f.close()

f = open("Sample0.json","r")

data = json.load(f)

print(data)

f.close()