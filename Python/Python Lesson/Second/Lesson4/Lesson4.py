print("1から10までの偶数を表示します。")
for i in range(10):
	if (i+1)%2 == 0:
		print(i+1)
        
print("1から10までの偶数を表示します。")
for i in range(2,11,2):
    print(i)

for i in range(9):
    for j in range(9):
        print((i+1)*(j+1),"\t",end="")
    print()
    
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()