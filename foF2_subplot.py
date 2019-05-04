import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np 
import pandas as pd 
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime


#initialize variables Main DST
y1 = pd.read_excel('Data/fof2.xlsx')
customdate = datetime.datetime(2015, 3, 1, 0)
x1 = [customdate + datetime.timedelta(hours=i) for i in range(len(y1))]

#subplot main DST
plt.subplot(2, 1, 1)
formatter = mdates.DateFormatter('%d')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.plot(x1, y1, 'b', linewidth=0.75)
plt.ylabel('foF2 $(Mhz)$')
plt.grid(linestyle='dotted')

#initialize variables Subplot DST
y2 = pd.read_excel('Data/fof2_subplot.xlsx')
customdate = datetime.datetime(2015, 3, 15, 0)
x2 = [customdate + datetime.timedelta(hours=i) for i in range(len(y2))]

#subplot DST zoomin
plt.subplot(2, 1, 2)
formatter = mdates.DateFormatter('%d')
plt.gcf().axes[1].xaxis.set_major_formatter(formatter)
plt.plot(x2, y2, 'b', linewidth=0.75)
plt.xlabel('March 2015')
plt.ylabel('foF2 $(Mhz)$')
plt.grid(linestyle='dotted')

plt.show()