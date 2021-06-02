import datetime

dt = datetime.datetime.now()

print("現在は",dt,"です。")
print("年:",dt.year,"です。")
print("月:",dt.month,"です。")
print("日:",dt.day,"です。")

dt = dt + datetime.timedelta(days=1)
print("1日後は",dt,"です。")