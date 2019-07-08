import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# initialize variables
y1 = pd.read_excel('data/Dst_subplot17_21.xlsx', delimiter=',', header=None)
y2 = pd.read_excel('data/TEC_subplot17_21.xlsx', delimiter=',', header=None)
y3 = pd.read_excel('data/TEC_median17_21.xlsx', delimiter=',', header=None)
customdate = datetime.datetime(2015, 3, 18, 0)  # date start
x = [customdate + datetime.timedelta(hours=i) for i in range(len(y1))]

# plot config
fig, host = plt.subplots(figsize=(14, 7))
plt.grid(linestyle='dotted')
par1 = host.twinx()

p1, = host.plot(x, y1, "r-", label="Dst Indeks")
p2, = par1.plot(x, y2, "black", label="TEC")
p3, = par1.plot(x, y3, 'gold', label="Median TEC")

# add minor grid
host.minorticks_on()
par1.minorticks_on()


host.set_xlabel("Maret 2015")
host.set_ylabel("Indeks DST $(nT)$")
par1.set_ylabel("TEC $(TECU)$")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2, p3]

host.legend(lines, [l.get_label() for l in lines], loc='lower right', prop={'size': 8.5})
formatter = mdates.DateFormatter('%d')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)

# minor grid activated
host.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()
