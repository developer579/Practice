sale = [80,60,22,50,75]

i = int(input("何番のリストを変更しますか？"))
num = int(input("変更後のデータを入力してください。"))

print(i,"番のデータを",num,"に変更します。")

sale[i] = num

print(i,"番のデータは",sale[i],"に変更されました。")