import pandas as pd

data_frame = {"a": [1, 4, 6, 7, 8], "b": [23, 12, 56, 8, 22], "c": [87, 65, 43, 11, 34]}

df = pd.DataFrame(data_frame)

print(df)

print("In ra cột đầu của dataframe")
print(df['b'])

print("In ra hàng đầu tiên của dataframe")
print(df.loc[0])



series_ex = pd.Series([1,2,3])
print(series_ex)
print('phan tu dau tien  cua series')

print(series_ex[0])
