str = ["Sample.csv","Sample.exe","Sample1.py","Sample2.py","Sample.txt","index.txt"]
file = []

print("ファイルのリストは以下の通りです。")
for s in str:
    print(s)

suf = input("拡張子を入力してください。")

for s in str:
    res = s.endswith(suf)
    if res is True:
        file.append(s)

print("該当するファイルのリストは以下です。")
for f in file:
    print(f)