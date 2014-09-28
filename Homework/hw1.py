import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

## Homework | Based Off Template of QSTK Tutorial 1

ls_symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
dt_start = dt.datetime(2006, 1, 1)
dt_end = dt.datetime(2010, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))

na_price = d_data['close'].values
plt.clf()
plt.plot(ldt_timestamps, na_price)
plt.legend(ls_symbols)
plt.ylabel('Adjusted Close')
plt.xlabel('Date')
plt.savefig('adjustedclose.pdf', format='pdf')

na_normalized_price = na_price / na_price[0, :]

na_rets = na_normalized_price.copy()
tsu.returnize0(na_rets)

plt.scatter(na_rets[:, 3], na_rets[:, 1], c='blue')

## vol, daily_ret, sharpe, cum_ret = 
## simulate(startdate, enddate, ['GOOG','AAPL','GLD','XOM'], [0.2,0.3,0.4,0.1])
## function should return:
## Standard deviation of daily returns of the total portfolio
## Average daily return of the total portfolio
## Sharpe ratio (Always assume you have 252 trading days in an year. 
## And risk free rate = 0) of the total portfolio
## Cumulative return of the total portfolio
def simulate(start_date, end_date, symbols, allocations):
	print 'starting simimulation'
	ldt_timestamps = du.getNYSEdays(start_date, end_date, dt_timeofday)
	ldf_data = c_dataobj.get_data(ldt_timestamps, symbols, ls_keys)
	d_data = dict(zip(ls_keys, ldf_data))
	na_price = d_data['close'].values
	na_normalized_price = na_price / na_price[0, :]

	na_rets = na_normalized_price.copy()
	daily_ret = tsu.returnize0(na_rets)



	## sqStdDev = np.std(squareArray)
	print na_price
	print na_normalized_price
	print na_rets
	print daily_ret

def run():
	print 'Running HW1 Script'
	dt_start = dt.datetime(2006, 1, 1)
	dt_end = dt.datetime(2010, 12, 31)
	ls_symbols = ['GOOG','AAPL','GLD','XOM']
	ls_allocation = [0.2,0.3,0.4,0.1]
	simulate(dt_start,dt_end,ls_symbols,ls_allocation)


run()
