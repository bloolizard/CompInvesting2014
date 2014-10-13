import pandas as pd
import numpy as np
import math
import copy
import QSTK.qstkutil.qsdateutil as du
import datetime as dt
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkstudy.EventProfiler as ep
import sys
import csv

## read in the dates and symbols

if __name__ == '__main__':
	print 'Starting simulator...'
	
	# order list is the first argument in command line
	orderlist_file = sys.argv[1]

	# per read in a csv file
	reader = csv.reader(open(orderlist_file,'rU'), delimiter=',')
	
	# make a list for dates
	dates_list = []
	# make a list for symbols
	symbols_list = []
	
	for row in reader:
		print row
		#append dates	
		dates_list.append(row[0:3])
		#append symbols
		symbols_list.append(row[3])

	print dates_list

	#remove duplicates
	symbols_list = list(set(symbols_list))
	print symbols_list
	