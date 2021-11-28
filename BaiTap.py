import pandas as pd
series_ex = {"a":[1, 4, 6, 7, 8], "b":[23, 12, 56, 8, 22], "c":[87, 65, 43, 11, 34]}
series_data = pd.DataFrame(series_ex)
print(series_data)
print("Xuat ra cot dau cua series")
print(series_data.iloc[:, 0])