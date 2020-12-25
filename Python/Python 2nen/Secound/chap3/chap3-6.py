import pandas as pd

df = pd.read_csv("test.csv")

print("「名前」の列を削除"+"\n",df.drop("名前",axis=1))
print("インデックス2の行を削除"+"\n",df.drop(2,axis=0))