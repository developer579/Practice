sale = [80,60,22,50,75]
i = int(input("何番のデータを変更しますか？"))
n = int(input("変更後のデータを入力してください。"))
print(i,"番のデータ",sale[i],"を変更します。")
sale[i] = n
print(i,"番のデータは",sale[i],"に変更されました。")