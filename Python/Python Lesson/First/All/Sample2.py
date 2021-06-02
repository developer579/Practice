print("数値を出力する。",1,)
print("数値を出力する。",3.14,)  
sale=10
print("売上は",sale,"万円です。")
sale=20
print("売上は",sale,"万円です。")
sale = float(input("売上を入力してください。")) 
if sale >= 100:
    print("売上は好調です。")
elif sale >=50:
    print("売上は普通です。")
else:
    print("売上は低調です。")
print("処理を終了します。")
sale=[80,60,22,50,75]

print(sale[0])
print(sale[1])
print(sale[2])
print(sale[3])
print(sale[4])
print("リストの長さは",len(sale),"です。")
sale = {"東京":80,"名古屋":60,"京都":22,"大阪":50,"福岡":75}
print("現在のデータは",sale,"です。")

k = input("どのキーのデータを表示しますか？")
if k in sale:
    print(k,"のデータは",sale[k],"です。")
else:
    print(k,"のデータは見つかりませんでした。")                                                                  