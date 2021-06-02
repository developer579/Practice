import os
import os.path

curdir = os.listdir()

print("名前",end="\t")
print("サイズ")

for name in curdir:
    print(name,end="\t")
    print(os.path.getsize(name),"バイト")
    
import os
import os.path
import datetime

curdir = os.listdir()

print("名前",end="\t")
print("最終アクセス時刻")

for name in curdir:
    atime = os.path.getatime(name)
    print(name,end="\t")
    print(datetime.datetime.fromtimestamp(atime))