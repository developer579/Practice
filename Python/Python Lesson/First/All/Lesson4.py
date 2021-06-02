print("1から10までの偶数を表示します。")
for i in range(10):
    if (i+1) % 2 == 0:
	    print(i+1)
    print()
print("1から10までの偶数を表示します。")
for i in range(2,11,2):
    print(i)
print()
print("九九の表を表示します。")
for i in range(1,10):
    for j in range(1,10):
        print(i*j,"\t",end = " ")
    print()
print("画面にコードを出力します。")
for i in range(1,6):
    for j in range(i):
        print("*",end = " ")
    print()
