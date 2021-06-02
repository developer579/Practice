import re

ptr = ["[1-2]","[0-3]","[^012]"]
str = ["0","1","2","3"]

for valueptr in ptr:
	print("------")
	pattern = re.compile(valueptr)
	for valuestr in str:
		res = pattern.search(valuestr)
		if res is not None:
			m = "o"
		else:
			m = "x"
		mrs = "(パターン)" + valueptr + "(文字列)" + valuestr + "マッチ" + m
		print(mrs)