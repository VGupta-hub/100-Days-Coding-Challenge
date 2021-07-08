import pandas as pd

data = pd.read_csv('C:/Users/vgupt/pandas/F-F_Research_Data_Factors.CSV')

row1 = data.iloc[3:6]
row1

row2 = data.iloc[3]
row2

row1 == row2

row1 = data.iloc[[3,4,5,6,7]]
row1

