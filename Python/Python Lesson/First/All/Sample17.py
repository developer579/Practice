test = [74,85,69,77,81]
ave = sum(test)/len(test)

print("テストの点は",test,"です。")
print("最高点数は",max(test),"です。")
print("最低点数は",min(test),"です。")
print("平均点は",ave,"です。")

print("テストの点は",test,"です。")
print("昇順は",sorted(test),"です。")
print("降順は",sorted(test,reverse=True),"です。")

high = [t for t in test if t >=80]
print("テストの点は",high,"です。")

