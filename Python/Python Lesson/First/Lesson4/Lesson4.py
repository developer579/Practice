print("1から10までの偶数を表示します。")
for i in range(1,11):
	if i%2 == 0:
	    print(i)
        
print("1から10までの偶数を表示します。")
for i in range(2,11,2):
    print(i)
    
print("九九の表を表示します。")
for i in range(1,10):
    for n in range(1,10):
        print(i*n,"\t",end="")
    print()
print("*のコードを出力します。")
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()