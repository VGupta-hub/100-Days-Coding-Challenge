import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2017,1,3)
end = dt.datetime(2021,5,7)

# ticker_symbol : input("Enter Stock Ticker: ")
# print(ticker_symbol)

prices = web.DataReader("AAPL", 'yahoo', start, end)['Close']

#Calulate returns
returns = prices.pct_change()

#Extract the last price
last_price = prices[-1]
# print(last_price)

#Defining the variable of simulation

#1.Number of simulations, time horizon
num_simulations = 1000
num_days = 252

#Create a df for all the simulations
simulation_df = pd.DataFrame()

#Simulation
for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    price_series = []
    price = last_price * (1+np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1+np.random.normal(0, daily_vol))
        price_series.append(price)
        count= count + 1

    simulation_df[x] = price_series

#Plotting our simulation

fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: AAPL')
plt.plot(simulation_df)
plt.axhline(y= last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()


