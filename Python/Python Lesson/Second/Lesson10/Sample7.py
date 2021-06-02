import os
import os.path

curdir = os.listdir()

for i in curdir:
	print(os.path.abspath(i),end="")
	
	if (os.path.isfile(i)):
		print("ファイルです。")
	else:
		print("ディレクトリです。")
print()