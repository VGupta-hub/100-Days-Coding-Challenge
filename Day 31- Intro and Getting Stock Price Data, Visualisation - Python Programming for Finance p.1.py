pip install pandas-datareader

import pandas as pd
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from pandas_datareader import data as pdr
import datetime as dt
style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime.now()

df = pd.read_csv("C:/NVDA.csv")
print(df.head(10))

df.to_csv(r'C:/Users/vgupt/Desktop/NVDA.csv', index=False, header=True)

df = pd.read_csv('C:/Users/vgupt/Desktop/NVDA.csv', parse_dates = True, index_col=0)
print(df)

By default, date columns are represented as object when loading data from a CSV file. To read the date column correctly, we can use the argument parse_dates to specify a list of date columns

# Visualization

df[['Open', 'Adj Close']].plot()

