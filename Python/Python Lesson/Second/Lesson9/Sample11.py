import re

ptr = ["(TXT)+","TXT|XTX"]
str = ["TX","TXT","XTX","TXTXT"]

for valueptr in ptr:
	print("------")
	pattern = re.compile(valueptr)
	for valuestr in str:
		res = pattern.search(valuestr)
		if res is not None:
			m = "o"
		else:
			m = "x"
		mrs = "(パターン)" + valueptr + "文字列" + valuestr + "マッチ" + m
		print(mrs)