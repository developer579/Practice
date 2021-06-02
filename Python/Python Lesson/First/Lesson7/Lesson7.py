def rpast(num):
	print("*" * num)
n = int(input("個数を入力してください。"))

rpast(n)

def rpstr(num,str="*"):
	print(num*str)

n = input("文字列を入力してください。")
s = int(input("個数を入力してください。"))

print("文字列あり---")
rpstr(n,s)
print("文字列なし---")
rpstr(s)

def makex(x):
    while True:
        yield x
        x = x+1
        
start = int(input("開始値（整数）を入力してください。"))
stop = int(input("停止値（整数）を入力してください。"))

for i in makex(start):
    if i >= stop:
        break
    print(i)