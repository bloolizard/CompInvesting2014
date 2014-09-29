import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## Homework | Based Off Template of QSTK Tutorial 1

ls_symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
dt_start = dt.datetime(2006, 1, 1)
dt_end = dt.datetime(2010, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
ls_allocation = [0.2,0.3,0.4,0.1]

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
	ldt_timestamps = du.getNYSEdays(start_date, end_date, dt_timeofday)
	ldf_data = c_dataobj.get_data(ldt_timestamps, symbols, ls_keys)
	d_data = dict(zip(ls_keys, ldf_data))
	na_price = d_data['close'].values
	na_normalized_price = na_price / na_price[0, :]


	na_rets = na_normalized_price.copy()
	
	
	na_portrets = np.sum(na_rets * allocations, axis=1)
	cum_ret = na_portrets[-1]

	tsu.returnize0(na_portrets)

	avg_daily_return = np.mean(na_portrets)
	std_dev = np.std(na_portrets)

	k = np.sqrt(250)
	sharpe_ratio = k * avg_daily_return/std_dev




	## sqStdDev = np.std(squareArray)
	return std_dev, avg_daily_return, sharpe_ratio, cum_ret

def run():
	print 'Running HW1 Script'
	dt_start = dt.datetime(2010, 1, 1)
	dt_end = dt.datetime(2010, 12, 31)
	ls_symbols = ['BRCM','ADBE','AMD','ADI']
	ls_allocation = [0.4,0.4,0.0,0.2]
	simulate(dt_start,dt_end,ls_symbols,ls_allocation)

def test_1():
	print 'Running Test 1'
	dt_start = dt.datetime(2011, 1, 1)
	dt_end = dt.datetime(2011, 12, 31)
	ls_symbols = ['AAPL','GLD','GOOG','XOM']
	ls_allocation = [0.4,0.4,0.0,0.2]
	print simulate(dt_start,dt_end,ls_symbols,ls_allocation)


## Create a for loop (or nested for loop) that enables you to test every "legal" set of allocations to the 4 stocks. 
## Keep track of the "best" portfolio, and print it out at the end.
##
def run_opt():
	print 'Running Portfolio Optimizer'
	dt_start = dt.datetime(2010, 1, 1)
	dt_end = dt.datetime(2010, 12, 31)
	ls_symbols = ['AAPL','GOOG','IBM','MSFT']
	ls_allocation = [0.4,0.4,0.0,0.2]
	

	lf_alloc = [0.0, 0.0, 0.0, 0.0]
	max_sharpe = -1000
	final_stddev = -1000
	final_dly_return = -1000
	final_cum_ret = -1000
	best_portfolio = lf_alloc


	for i in range(0, 101, 10):
		left_after_i = 101 - i
		for j in range(0, left_after_i, 10):
			left_after_j = 101 - i - j
			for k in range(0, left_after_j, 10):
				left_after_k = 100 - i - j - k
				lf_alloc = [i, j, k, left_after_k]
				std, dly_rt, sharpe, cum_ret = simulate(dt_start, dt_end, ls_symbols, lf_alloc)
				if sharpe > max_sharpe:
					max_sharpe = sharpe
					final_stddev = std
					final_cum_ret = cum_ret
					final_dly_return = dly_rt
					best_portfolio = lf_alloc

	print "Best Portfolio: ",  best_portfolio
	print "Max Sharpe: ", max_sharpe
	print "Final STD", final_stddev
	print "Final Cum Return: ", final_cum_ret
	print "Final Daily Return: ", final_dly_return

run_opt()