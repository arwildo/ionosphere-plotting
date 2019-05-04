import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np 
import pandas as pd 
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime


#initialize variables
y1 = pd.read_excel('data/Dst_subplot.xlsx'
	, delimiter=',', header=None)
y2 = pd.read_excel('data/fof2_subplot.xlsx'
	, delimiter=',', header=None)
customdate = datetime.datetime(2015, 3, 15, 0) #date start
x = [customdate + datetime.timedelta(hours=i) for i in range(len(y1))]


#plot config
fig, host = plt.subplots(figsize=(10,5))
plt.grid(linestyle='dotted')
par1 = host.twinx()

p1, = host.plot(x, y1, "r-", label="Dst Indeks")
p2, = par1.plot(x, y2, "b-", label="foF2")


host.set_xlabel("March 2015")
host.set_ylabel("Dst Indeks $(nT)$")
par1.set_ylabel("foF2 $(Mhz)$")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2]

host.legend(lines, [l.get_label() for l in lines])
formatter = mdates.DateFormatter('%d')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)



plt.show()