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

print(simulation_df)

### Output:
            0           1           2    ...         997         998         999
0    131.710122  130.700599  128.005966  ...  129.771275  130.944465  133.193652
1    137.168184  130.714608  131.313611  ...  127.172730  133.238826  133.641256
2    138.127851  131.211455  131.021639  ...  122.780701  134.377752  131.087921
3    136.622162  131.856990  131.598934  ...  118.549861  137.022143  128.318533
4    136.991955  134.204312  131.287270  ...  116.268272  141.313616  128.526834
..          ...         ...         ...  ...         ...         ...         ...
247  155.666843  129.613311   80.986903  ...  171.292879  149.336294  119.284558
248  152.515765  130.139159   82.264541  ...  165.859745  152.961730  118.281468
249  150.306416  133.018154   82.504727  ...  157.394981  152.304013  120.046786
250  150.179352  131.689777   82.663632  ...  153.451341  150.351722  120.822600
251  147.632649  131.913280   83.522955  ...  155.901174  148.650398  119.967125
    
    
#Plotting our simulation

fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: AAPL')
plt.plot(simulation_df)
plt.axhline(y= last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()

# Output:
https://user-images.githubusercontent.com/83883988/118217839-439bec80-b444-11eb-9a4d-420a4ac730ff.png
