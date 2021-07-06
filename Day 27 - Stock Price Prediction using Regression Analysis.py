pip install yfinance

# importing all the modules/libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

import yfinance as yf

Collecting data about the company's business, stock prices, volumes and corporate actions associated with the stock by its Ticker Symbol from YFinance

nio = yf.Ticker("NIO")
nio.info

Collecting data about the company's business, stock prices, volumes and corporate actions associated with the stock.

Preparing and cleaning the data for Regression Analysis

history = nio.history(period = "Max")
df = pd.DataFrame(history)
df.head(10)

Defining x and y 

x = df.index
y = df['Close']
y

Exploring the data

stock_name = input("Enter the stock ticker: ")
title = (stock_name, "Historical stock performance till date")


Defining a plot function for this analysis

def df_plot(data, x, y, title="", xlabel = "Date", ylabel = "Value", dpi =100):
    plt.figure(figsize=(16,5), dpi = dpi)
    plt.plot(x,y, color = "tab:red")
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

df_plot(df, x, y, title=title, xlabel = "Date", ylabel = "Value", dpi =100)

# Resetting index and converting it to column
df.reset_index(inplace=True)
df.head(2)

df["Date"] = pd.to_datetime(df.Date)
df.describe()

print(len(df))

x = df[["index", "Open", "High", "Low", "Volume", "Dividends", "Stock Splits"]]
y = df["close"]

