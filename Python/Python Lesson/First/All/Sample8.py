n = input("値を入力してください。")
print(n,"が入力されました")
num = int(input("何月の処理で終了しますか？"))
for i in range(12):
    print(i+1,"月のデータです。")
    if(i+1) == num:
        break
        
data1 = [1,2,3,4,5]
data2 = list(data1)

print("data1は",data1,"です。")
print("data2は",data2,"です。")

data1[0] = 10

print("data1は",data1,"です。")
print("data2は",data2,"です。")