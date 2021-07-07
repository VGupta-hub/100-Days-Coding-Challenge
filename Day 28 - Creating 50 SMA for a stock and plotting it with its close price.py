import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

yf.pdr_override() #activate yahoo finance workaround
now = dt.datetime.now() #Runs until todays date
stock = input("Enter the stock ticker: ") #Query user for stock ticker

startyear = 2019
startmonth = 1
startday = 1
start = dt.datetime(startyear, startmonth, startday) # set starting time for datasample
now = dt.datetime.now()

df = pdr.get_data_yahoo(stock,start, now)
print(df)

ma = 50
smaString = "SMA_" + str(ma)
ema = 30
emaString = "EMA_" + str(ma)

df[smaString] = df.iloc[:,4].rolling(window=ma).mean() #creating a simple moving average from the fourth column (close) in our dataframe usine pandas

print(df)

Removing first 50 rows as they don't have values for SMA

df=df.iloc[ma:]
print(df)

Iterating thorugh each trading day and creating a check to see if the closing price was above or below the moving average

for i in df.index:
    print(df[smaString][i]) #this is gonna print the SMA for each date which is i in this df

Comparing the two values with an if statement

for i in df.index:
    if(df["Adj Close"][i]>df[smaString][i]):
        print("The close is higher than SMA.")
    else:
        print("The close is lower than SMA.")

Counting the number of times the close was higher or lower

numH = 0
numC = 0

for i in df.index:
    if(df["Adj Close"][i]>df[smaString][i]):
#         print("The close is higher than SMA.")
        numH = numH + 1
    else:
#         print("The close is lower than SMA.")
        numC = numC + 1
print("The close is higher than SMA {} times.".format(str(numH)))
print("The close is lower than SMA {} times.".format(str(numC)))

x = df.index
y = df["Adj Close"]
z = df["SMA_50"]
z

Defining a plot function for this analysis

title = (stock, "Adjusted Close price till date and 50 SMA")

def df_plot(data, x, y, title="", xlabel = "Date", ylabel = "Adj Close", dpi =100):
    plt.figure(figsize=(16,5), dpi = dpi)
    plt.plot(x,y, color = "tab:blue")
    plt.plot(z, color = "tab:red")
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

df_plot(df, x, y, title=title, xlabel = "Date", ylabel = "Value", dpi =100)

# Checkout this link for the plot

https://user-images.githubusercontent.com/83883988/124818372-f36b7300-df38-11eb-9a7f-29a0778ecfa8.png
