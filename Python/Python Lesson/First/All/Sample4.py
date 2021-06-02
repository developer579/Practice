print("水平タブを表示します。:\t")
print("垂直タブを表示します。:\v")
print("改行を表示します。:\n")
print("復帰を表示します。:\r")
print("警告音を表示します。:\a")
print("バックスペースを表示します。:\b")
print("改ページを表示します。:\f")
print("\'を表示します。:\'")
print("\"を表示します。:\"")
print("\345を表示します。:\345")
print("\xFFを表示します。:\xFF")
print("1+2は",1+2,"です。")
for i in range(1,13,1):
    print(i,"月のデータです。")
sale = [80,60,22,50,75]

i = int(input("何番のデータを変更しますか？"))
num = int(input("変更後のデータを入力してください。"))

print(i,"番のデータ",sale[i],"を変更します。")

sale[i] = num

print(i,"番のデータは",sale[i],"に変更されました。")

for s in sale:
    print(s)
print("リストの長さは",len(sale),"です。")

sale = {"東京":80,"名古屋":60,"京都":22,"大阪":50,"福岡":75}
print("現在のデータは",sale,"です。")

print("キーを表示します。")
for k in sale.keys():
    print(k,end="\t")
print()

print("値を表示します。")
for v in sale.values():
    print(v,end="\t")
print()

print("キーと値を表示します。")
for i in sale.items():
    print(i,end="")
print()