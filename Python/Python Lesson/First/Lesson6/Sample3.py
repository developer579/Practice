sale = {"東京":80,"名古屋":60,"京都":22,"大阪":50,"福岡":75}
print("現在のデータは",sale,"です。")
c = input("追加するキーを入力してください。")
if c in sale:
	print(c,"のデータはすでに存在しています。")
else:
	d = input("追加するデータを入力してください。")
	sale[c] = d
	print(c,"のデータとして",sale[c],"を追加しました。")
print("現在のデータは",sale,"です。")
c1 = input("どのキーのデータを変更しますか？")
if c1 in sale:
	d1 = input("追加するデータを入力してください。")
	sale[c1] = d1
	print(c1,"のデータは",sale[c1],"に変更されました。")
else:
	print(c1,"のデータはみつかりませんでした。")
print("現在のデータは",sale,"です。")
c2 = input("どのキーのデータを削除しますか？")
if c2 in sale:
	print(c2,"のデータは",sale[c2],"です。")
	del sale[c2]
	print("データを削除しました。")
else:
	print(c2,"のデータはみつかりませんでした。")
print("現在のデータは",sale,"です。")