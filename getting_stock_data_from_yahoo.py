import pandas_datareader as pdr
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gild = pdr.get_data_yahoo('GILD',
                          start=datetime.datetime(2006, 10, 1),
                          end=datetime.datetime(2020, 11, 4))
'''
### getting columns
col = gild.columns
print (col)

### getting last 10 close prices
ts = gild['Close'][-10:]
print (ts)

# Inspect the first rows of 2020
print(gild.loc['2020'].head())
'''

daily_close = gild[['Adj Close']]
daily_pct_change = daily_close.pct_change()
daily_pct_change.fillna(0, inplace=True)
print(daily_pct_change)
daily_log_returns_shift = np.log(daily_close / daily_close.shift(1))
print(daily_log_returns_shift)
cum_daily_return = (1 + daily_pct_change).cumprod()

# Resample to business months, take last observation as value
monthly = gild.resample('BM').apply(lambda x: x[-1])
monthly.pct_change()
# Resample to quarters, take the mean as value per quarter
quarter = gild.resample("4M").mean()
quarter.pct_change()

# Chart zeichnen
plt.style.use('gadfly')
gild['Close'].plot(grid=True)
cum_daily_return.plot(figsize=(12,8))
plt.show()
