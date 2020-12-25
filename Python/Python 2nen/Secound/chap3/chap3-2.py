import pandas as pd

df = pd.read_csv("test.csv")

print("データの個数=",len(df))
print("項目名     =",df.columns.values)
print("インデックス=",df.index.values)