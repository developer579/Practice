list = ["Sample.csv","Sample.exe","Sample1.py","Sample2.py","Sample.txt","index.html"]
file = []

print("ファイルのリストは以下です。")
for i in list:
	print(i)

key = input("拡張子を入力してください。")
for i in list:
    res = i.endswith(key)
    if res is True:
        file.append(i)
print("該当するファイルのリストは以下です。")
for i in file:
    print(i)