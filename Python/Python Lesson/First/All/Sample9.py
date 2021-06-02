num1 = float(input("整数1を入力してください。"))
num2 = float(input("整数2を入力してください。"))
num3 = num1 + num2
print(num1,"+",num2,"は",num3,"です。")
num = int(input("何月の処理を飛ばしますか？(1〜12)"))
for i in range(12):
    if (i+1) == num:
        continue
    print(i+1,"月のデータです。")
sale1 = [1,2,3,4,5,6]
print("上半期のデータは",sale1,"です。")

sale2 = [7,8,9,10,11,12]
print("下半期のデータは",sale2,"です。")

ysale = sale1 + sale2

print("年間のデータは",ysale,"です。")