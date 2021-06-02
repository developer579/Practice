num = 10
pic = "◯"
graph = pic * num
print("売上：" + graph)
print(num , "万円の売上があります。")
v = False
for i in range(5):
    for j in range(5):
        if v is False:
            print("*",end=" ")
            v = True
        else:
            print("-",end=" ")
            v = False
    print()
data1 = [1,2,3,4,5]
data2 = data1

print("data1は",data1,"です。")
print("data2は",data2,"です。")

data1[0] = 10

print("data1を変更します。")

print("data1は",data1,"です。")
print("data2は",data2,"です。")

cityA = {"東京","名古屋","京都","大阪"}
cityB = {"京都","大阪","福岡"}

print("Aの都市名は",cityA,"です。")
print("Bの都市名は",cityB,"です。")

print("共通するデータは",cityA & cityB,"です。")
print("Aのみのデータは",cityA - cityB,"です。")
print("Bのみのデータは",cityB - cityA,"です。")
print("すべてのデータは",cityA | cityB,"です。")