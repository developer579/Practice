sale1 = {"東京":80,"名古屋":60,"京都":22}
sale2 = {"京都":100,"大阪":50,"福岡":75}

print("1のデータは",sale1,"です。")
print("2のデータは",sale2,"です。")

print("1を2で更新します。")

sale1.update(sale2)

print("1のデータは",sale1,"です。")