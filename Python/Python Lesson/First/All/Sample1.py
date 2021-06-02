#画面に出力する
print("ようこそpythonへ！")
print("Pythonをはじめましょう！")
sale=10
print("売上は",sale,"万円です。")
sale = int(input("売上を入力してください。"))
if sale >= 100 :
	print("売上は好調です。")
if sale <= 100 :
    print("売上は不調です。")
print("処理を終了します。")
sale=[80,60,22,50,75]
print(sale)

sale = {"東京":80,"名古屋":60,"京都":22,"大阪":50,"福岡":75}
print("現在のデータは",sale,"です。")

k = input("どの支店のデータを表示しますか？")
print(k,"のデータは",sale[k],"です。")