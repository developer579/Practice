test = [74,85,69,77,81]
print("テストの点は",test,"です。")
print("最高点は",max(test),"です。")
print("最低点は",min(test),"です。")
total = sum(test)
print("平均点は",(total/len(test)),"です。")

print("テストの点は",test,"です。")
print("昇順は",sorted(test),"です。")
print("降順は",sorted(test,reverse=True),"です。")

print("テストの点は",test,"です。")
high = [t for t in test if t >= 80]
print("80点以上は",high,"です。")
print("80点以上の人数は",len(high),"人です。")

city = ["東京","名古屋","大阪","京都","福岡"]
ht = [32,28,27,26,27]
lt = [25,21,20,19,22]
print("都市名データは",city,"です。")
print("最高気温データは",ht,"です。")
print("最低気温データは",lt,"です。")

for c,h,l in zip(city,ht,lt):
    print(c,"の最高気温は",h,"最低気温は",l,"です。")