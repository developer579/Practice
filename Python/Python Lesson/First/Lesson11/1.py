sale = [80,60,22,50,75]
num = int(input("何番のデータを変更しますか？"))
if (num+1) <= len(sale):
    print(num,"番のデータを変更します。")
    sale[num] = int(input("変更後のデータを入力してください。"))
    print(num,"番のデータを",sale[num],"に変更しました。")
else:
    print(num,"番のデータはみつかりませんでした。")
    q = input("データを追加しますか？(YES,NO)")
    if q == "YES" or q == "yes" or q == "Yes":
        print(len(sale),"番にデータを追加します。")
        data = int(input("追加するデータを入力してください。"))
        sale.insert(len(sale),data)
        print(len(sale)-1,"番に",sale[(len(sale)-1)],"を追加しました。")
print("現在のデータは",sale,"です。")
print("処理を終了します。")