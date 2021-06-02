print("10進数の10は",10,"です。")
print("2進数の10は",0b10,"です。")
print("8進数の10は",0o10,"です。")
print("16進数の10は",0x10,"です。")
print("16進数のFは",0xF,"です。")
print("",123,"\n\\",100,"もらった\nまたあした")
name="東京"
sale=10
print(name,"支店の売上は",sale,"万円です。")
sale = float(input("売上を入力してください。"))
num = int(input("人数を入力してください。"))
if sale >= 100 and num >=30 :
    print("売上は大盛況です。")
elif sale >= 100 :
    print("売上は好調です。")
elif sale >= 50 :
    print("売上は普通です。")
else:
    print("売上は低調です。")
print("処理を終了します。")
sale = [80,60,22,50,75]
for s in sale:
    print(s)
print("リストの長さは",len(sale),"です。")

sale= {"東京":80,"名古屋":60,"京都":22,"大阪":50,"福岡":75}
print("現在のデータは",sale,"です。")

k = input("追加するキーを入力してください。")
if k in sale:
    print(k,"のデータはすでに存在しています。")
else:
    d = int(input("追加するデータを入力してください。"))
    sale[k] = d
    print(k,"のデータとして",sale[k],"を追加しました。")

k = input("どのキーのデータを追加しますか？")
if k in sale:
    print(k,"のデータは",sale[k],"です。")
    d = int(input("データを入力してください。"))
    sale[k] = d
    print(k,"のデータは",sale[k],"に変更されました。")
else:
    print(k,"のデータはみつかりませんでした。")
print("現在のデータは",sale,"です。")

k = input("どのキーのデータを削除しますか？")
if k in sale:
    print(k,"のデータは",sale[k],"です。")
    del sale[k]
    print("データを削除しました。")
else:
    print(k,"のデータはみつかりませんでした。")
print("現在のデータは",sale,"です。")