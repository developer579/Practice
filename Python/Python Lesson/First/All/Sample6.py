num1 = 10
num2 = 5
print("num1+num2は",num1+num2,"です。")
print("num1-num2は",num1-num2,"です。")
print("num1*num2は",num1*num2,"です。")
print("num1/num2は",num1/num2,"です。")
print("num1%num2は",num1%num2,"です。")
for i in range(5):
    for j in range(3):
        print("iは",i,":jは",j)

sale = [80,60,22,50,75]
print("現在のデータは",sale,)

print("先頭のデータを削除します。")
del sale[0]
print("現在のデータは",sale,"です。")

print("22を削除します。")
sale.remove(22)
print("現在のデータは",sale,"です。")

city = {"東京","名古屋","京都","大阪","福岡"}
print("現在のデータは",city,"です。")

d = input("追加するデータを入力してください。")
if d in city:
    print(d,"はすでに存在しています。")
else:
    city.add(d)
    print(d,"を追加しました。")
print("現在のデータは",city,"です。")

d = input("削除するデータを入力してください。")
if d in city:
    city.remove(d)
    print(d,"を削除しました。")
else:
    print(d,"はみつかりませんでした。")
print("現在のデータは",city,"です。")