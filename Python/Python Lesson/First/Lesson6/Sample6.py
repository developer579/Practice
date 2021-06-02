city = {"東京","名古屋","京都","大阪","福岡"}
print("現在のデータは",city,"です。")
n = input("追加するデータを入力してください。")
if n in city:
	print(n,"はすでに存在しています。")
else:
	city.add(n)
	print(n,"を追加しました。")
print("現在のデータは",city,"です。")

n = input("削除するデータを入力してください。")
if n in city:
	city.remove(n)
	print(n,"を削除しました。")
else:
	print(n,"はみつかりませんでした。")
print("現在のデータは",city,"です。")