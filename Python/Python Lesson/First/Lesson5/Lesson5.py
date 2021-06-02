test = [74,85,69,77,81]
ave = sum(test)/len(test)
print("テストの点は",test,"です。")
print("最高点は",max(test),"です。")
print("最低点は",min(test),"です。")
print("平均点は",ave,"です。")

print("テストの点は",test,"です。")
print("テストの点は",sorted(test),"です。")
print("テストの点は",sorted(test,reverse=True),"です。")

print("テストの点は",test,"です。")
high = [n for n in test if n >= 80]
print("80点以上は",high,"です。")
print("80点以上の人数は",len(high),"人です。")

city = ["東京","名古屋","大阪","京都","福岡"]
tmp1 = [32,28,27,26,27]
tmp2 = [25,21,20,19,22]
for c,tm1,tm2 in zip(city,tmp1,tmp2):
    print(c,"の最高気温は",tm1,"最低気温は",tm2,"です。")