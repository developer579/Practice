price = 50
num = 10
total = price * num
print("単価は",price,"円です。")
print("売上個数は",num,"個です。")
print("合計金額は",total,"円です。")

total = total - 100

print("値引きすると",total,"円です。")

i = 1
while i <= 12:
    print(i,"月のデータです。")
    i = i+1
    
sale = [80,60,22,50,75]
print("現在のデータは",sale,"です。")

print("末尾に100を追加します。")
sale.append(100)
print("現在のデータは",sale,"です。")

print("sale[2]に25を挿入します。")
sale.insert(2,25)
print("現在のデータは",sale,"です。")

sale1 = {"東京":80,"名古屋":60,"京都":22}
sale2 = {"京都":100,"大阪":50,"福岡":75}

print("1のデータは",sale1,"です。")
print("2のデータは",sale2,"です。")

print("1を2で更新します。")

sale1.update(sale2)

print("1のデータは",sale1,"です。")