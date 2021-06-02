#Lesson1
print("ようこそPythonへ")

#Lesson2
print("ようこそPythonへ")
print("Pythonをはじめましょう")

print(1)
print(3.14)

print("10進数の10は",10,"です。")
print("2進数の10は",0b10,"です。")
print("8進数の10は",0o10,"です。")
print("16進数の10は",0x10,"です。")
print("16進数の10は",0xF,"です。")

print("バックスラッシュを表示します。:\\")
print("アポストロフィーを表示します。:\'")

print("数値を出力する。",1)
print("数値を出力する。",3.14)

print(123)
print("\\",100,"もらった")
print("またあした")

print(1,"\t",2,"\t",3,"\t",4,"\t",5,"\t",6)

#Lesson3
sale = 10
print("売上は",sale,"万円です。")

sale = 10
print("売上は",sale,"万円です。")
print("売上の値を変更します。")
sale = sale + 10
print("売上は",sale,"万円です。")

name = "東京"
sale = 10
print(name,"支店の売上は",sale,"万円です。")

print("1+2は",1+2,"です。")

price = 50
num = 10
total = price * num
print("単価は",price,"です。")
print("売上個数は",num,"です。")
print("合計金額は",total,"です。")
total = total - 100
print("値引きすると",total,"です。")

num1 = 10
num2 = 5
print("num1+num2は",num1+num2,"です。")
print("num1-num2は",num1-num2,"です。")
print("num1*num2は",num1*num2,"です。")
print("num1/num2は",num1/num2,"です。")
print("num1%num2は",num1%num2,"です。")

num = 10
pic = "○"
graph = pic * num 
print("売上:" + graph)
print(num,"万円の売上があります。")

n = input("値を入力してください。")
print(n,"が入力されました。")

num1 = int(input("整数1を入力してください。"))
num2 = int(input("整数2を入力してください。"))
num3 = num1 + num2
print(num1,"+",num2,"は",num3,"です。")

age = int(input("あなたは何才ですか？"))
print("あなたは",age,"です。")

h = float(input("身長を入力してください。"))
w = float(input("体重を入力してください。"))
print("身長は",h,"センチです。")
print("体重は",w,"キロです。")

#Lesson4
sale = int(input("売上を入力してください。"))
if sale >= 100:
	print("売上は好調です。")
print("処理を終了します。")

sale = int(input("売上を入力してください。"))
if sale >= 100:
	print("売上は好調です。")
elif sale >= 50:
	print("売上は普通です。")
else:
	print("売上は低調です。")
print("処理を終了します。")

sale = int(input("売上を入力してください。"))
num = int(input("人数を入力してください。"))

if sale >= 100 and num >= 30:
	print("売上は大盛況です。")
elif sale >= 100:
	print("売上は好調です。")
elif sale >= 50:
	print("売上は普通です。")
else:
	print("売上は低調です。")
print("処理を終了します。")

for i in range(12):
	print(i+1,"月のデータです。")

i = 1
while i >= 12:
	print(i,"月のデータです。")
	i = i+1
	
for i in range(5):
	for j in range(3):
		print("iは",i,":jは",j)

v = False
for i in range(5):
	for j in range(5):
		if v is False:
			print("*",end="")
			v = True
		else:
			print("-",end="")
			v = False
	print()

num = int(input("何月の処理で終了しますか？(1〜12)"))
for i in range(12):
	print(i+1,"月のデータです。")
	if (i+1) == num:
		break

num = int(input("何月の処理を飛ばしますか？(1〜12)"))
for i in range(12):
	if (i+1) == num:
		continue
	print(i+1,"月のデータです。")
	
print("1から10までの偶数を表示します。")
for i in range(1,11):
	if (i%2) == 0:
		print(i)
		
print("1から10までの偶数を表示します。")
for i in range(2,11,2):
	print(i)
	
for i in range(1,10):
	for j in range(1,10):
		print(i*j,"\t",end ="")
	print()

for i in range(1,6):
	for j in range(i):
		print("*",end="")
	print()

#Lesson5
sale = [80,60,22,50,75]
print(sale)

sale = [80,60,22,50,75]
print(sale[0])
print(sale[1])
print(sale[2])
print(sale[3])
print(sale[4])
print("リストの長さは",len(sale),"です。")

sale = [80,60,22,50,75]
for i in sale:
	print(i)
print("リストの長さは",len(sale),"です。")

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

sale = [80,60,22,50,75]
print("現在のデータは",sale,"です。")
print("末尾に100を追加します。")
sale.append(100)
print("現在のデータは",sale,"です。")
print("sale[2]に25を挿入します。")
sale.insert(2,25)
print("現在のデータは",sale,"です。")

sale = [80,60,22,50,75]
print("現在のデータは",sale,"です。")
print("先頭のデータを削除します。")
del sale[0]
print("現在のデータは",sale,"です。")
print("22を削除します。")
sale.remove(22)
print("現在のデータは",sale,"です。")

data1 = [1,2,3,4,5]
data2 = data1
print("data1は",data1,"です。")
print("data2は",data2,"です。")
print("data1を変更します。")
data1[0] = 10
print("data1は",data1,"です。")
print("data2は",data2,"です。")

data1 = [1,2,3,4,5]
data2 = list(data1)
print("data1は",data1,"です。")
print("data2は",data2,"です。")
print("data1を変更します。")
data1[0] = 1
print("data1は",data1,"です。")
print("data2は",data2,"です。")

sale1 = [1,2,3,4,5,6]
print("上半期のデータは",sale1,"です。")
sale2 = [7,8,9,10,11,12]
print("下半期のデータは",sale2,"です。")
ysale = sale1 + sale2
print("年間のデータは",ysale,"です。")

ysale = [1,2,3,4,5,6,7,8,9,10,11,12]
print("年間のデータは",ysale,"です。")
sale1 = ysale[0:6]
print("上半期のデータは",sale1,"です。")
sale2 = ysale[6:]
print("下半期のデータは",sale2,"です。")
sale3 = ysale[::2]
print("一ヵ月おきのデータは",sale3,"です。")
sale4 = ysale[::-1]
print("逆順のデータは",sale4,"です。")
print("年間のデータは",ysale,"です。")
print("上半期のデータを差し替えます。")
ysale[0:6] = [0,0,0,0,0,0]
print("年間のデータは",ysale,"です。")

data = [1,2,3,4,5]
print("現在のデータは",data,"です。")
print("data[::-1]をfor文で処理します。")
for i in data[::-1]:
	print("data[::-1]は",i,"です。")
print("現在のデータは",data,"です。")
print("reversed(data)をfor文で処理します。")
for i in reversed(data):
	print("reversed(data)は",i,"です。")
print("現在のデータは",data,"です。")
print("data.reverse()を処理します。")
data.reverse()
print("現在のデータは",data,"です。")

city = ['東京','名古屋','大阪','京都']
sale = [80,60,22,50,75]
print("都市名データは",city,"です。")
print("売上データは",sale,"です。")
print("データを組み合わせます。")
for d in zip(city,sale):
	print(d)
print("データとインデックスを組み合わせます。")
for d in enumerate(city):
	print(d)
	
city = ['東京','名古屋','大阪','京都']
sale = [80,60,22,50,75]
print("都市名データは",city,"です。")
print("売上データは",sale,"です。")
print("データを組み合わせます。")
for d in zip(city,sale):
	print(d)
print("データを分解します。")
for c,s in zip(city,sale):
	print("都市名は",c,"売上は",s)

data = [1,2,3,4,5]
print("現在のデータは",data,"です。")
ndata = [n*2 for n in data if d != 3]
print("新しいデータは",d,"です。")
	
sale = [80,60,22,50,75]
print("現在のデータは",sale,"です。")
print("最大のデータは",max(sale),"です。")
print("最小のデータは",min(sale),"です。")
print("データの合計は",sum(sale),"です。")
print("ソートされたデータは",sorted(sale),"です。")
print("ソートされたデータは",sorted(sale,reverse=True),"です。")
sale.sort(reverse=True)
print("ソートされたデータは",sale,"です。")

city = [
	['東京',32,25],
	['名古屋',28,21],
	['大阪',27,20],
	['京都',26,19],
	['福岡',27,22]
]
print("現在のデータは",city,"です。")
for c in city:
	print("都市別データは",c,"です。")
	for d in c:
		print(d,end="\t")
	print()
print(city[0][0],"の最高気温は",city[0][1],"最低気温は",city[0][2])

test = [74,85,69,77,81]
print("テストの点は",test,"です。")
print("最高点は",max(test),"です。")
print("最低点は",min(test),"です。")
ave = sum(test) / len(test)
print("平均点は",ave,"です。")

print("テストの点は",test,"です。")
print("昇順は",sorted(test),"です。")
print("降順は",sorted(test,reverse=True),"です。")

print("テストの点は",test,"です。")
high = [n for n in test if n >= 80]
print("80点以上は",high,"です。")