import os
import os.path

curdir = os.listdir()

print("名前","\t","サイズ")
for i in curdir:
	print(i,"\t",os.path.getsize(i),"バイト")

import datetime

print("名前","\t","最終アクセス時刻")
for i in curdir:
    print(i,"\t",datetime.datetime.fromtimestamp(os.path.getatime(i)))
