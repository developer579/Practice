import re

ptr = ["T","T+","T?","T{3}"]
str = ["X","TT","TTT","TTTT"]

for valueptr in ptr:
	print("------")
	pattern = re.compile(valueptr)
	for valuestr in str:
		res = pattern.search(valuestr)
		if res is not None:
			m = "o"
		else:
			m = "x"
		mrs = "(パターン)" + valueptr + "(文字列)" + valuestr + "(マッチ)" + m
		print(mrs)