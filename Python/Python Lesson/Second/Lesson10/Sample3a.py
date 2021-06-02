import csv

f = open("Sample0.csv","w")

wt = csv.writer(f)

wt.writerow(["東京","消しゴム"])
wt.writerows([["東京","消しゴム"],["名古屋","ノート"]])

f.close()

f = open("Sample0.csv","r")

rd = csv.reader(f)

for row in rd:
	for col in row:
		print(col,end="\t")
	print()
	
f.close()