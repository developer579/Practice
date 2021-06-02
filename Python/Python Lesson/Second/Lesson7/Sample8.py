def append():
	print("データを追加します。")
def updata():
	print("データを変更します。")
def delete():
	print("データを削除します。")

list = [append,updata,delete]

res = int(input("操作番号を入力してください。(0〜2)"))

if 0 <= res and res < len(list):
	list[res]()