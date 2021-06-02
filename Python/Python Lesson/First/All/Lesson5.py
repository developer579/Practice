test = [74,85,69,77,81]
ave = sum(test)/len(test)

print("テストの点は",test,"です。")
print("最高点数は",max(test),"です。")
print("最低点数は",min(test),"です。")
print("平均点は",ave,"です。")

print()

print("テストの点は",test,"です。")
print("昇順は",sorted(test),"です。")
print("降順は",sorted(test,reverse=True),"です。")

print()

high = [t for t in test if t >=80]
print("テストの点は",test,"です。")
print("80点以上は",high,"です。")
print("80点以上の人数は",len(high),"人です。")

print()

city = ["東京","名古屋","大阪","京都","福岡"]
data1 = [32,28,27,26,27]
data2 = [25,21,20,19,22]

print("都市名データは",city,"です。")
print("最高気温データは",data1,"です。")
print("最低気温データは",data2,"です。")

for c,d1,d2 in zip(city,data1,data2):
    print(c,"の最高気温は",d1,"最低気温は",d2,"です。")