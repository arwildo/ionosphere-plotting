import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np 
import pandas as pd 
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime


plt.figure(figsize=(8, 5))
customdate = datetime.datetime(2015, 3, 1, 0)

y = pd.read_excel('Data/DST.xlsx')
x = [customdate + datetime.timedelta(hours=i) for i in range(len(y))]

formatter = mdates.DateFormatter('%d %H')

plt.plot(x, y, 'b')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.xlabel('March 2015')
plt.ylabel('DST Index (nT)')

plt.show()