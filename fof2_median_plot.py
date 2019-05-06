import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime

#initialize variables
y1 = pd.read_excel('data/fof2_subplot.xlsx', delimiter=',', header=None)
y2 = pd.read_excel('data/fof2_median.xlsx', delimiter=',', header=None)
customdate = datetime.datetime(2015, 3, 15, 0)  #date start
x = [customdate + datetime.timedelta(hours=i) for i in range(len(y1))]

#plot config
fig, host = plt.subplots(figsize=(9, 4))
plt.grid(linestyle='dotted')

p1, = host.plot(x, y1, "blue", label="foF2")
p2, = host.plot(x, y2, "lime", label="median")

host.set_xlabel("March 2015")
host.set_ylabel("foF2 $(Mhz)$")

host.yaxis.label.set_color('black')
host.yaxis.label.set_color('black')

tkw = dict(size=3, width=1.5)
host.tick_params(axis='y', colors='black', **tkw)
host.tick_params(axis='y', colors='black', **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2]

host.legend(lines, [l.get_label() for l in lines], loc="lower right")
formatter = mdates.DateFormatter('%d')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)

plt.show()