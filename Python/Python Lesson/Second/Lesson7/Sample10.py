def deco(func):
	def wrapper(x):
		wx = "---" + x + "---"
		return func(wx)
	return wrapper

@ deco
def printmsg(x):
	print(x,"が入力されました。")

str = input("メッセージを入力してください。")
printmsg(str)