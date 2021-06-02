import sqlite3

conn = sqlite3.connect("pdb.db")

c = conn.cursor()

p = input("何円以上の結果を表示しますか？")

itr = c.execute("SELECT * FROM product WHERE price>=?",(p,))

for row in itr:
	print(row)
conn.close()