import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime

#initialize variables
y1 = pd.read_excel('data/TEC_analysis_median_df.xlsx',
                   delimiter=',',
                   header=None)
y2 = pd.read_excel('data/TEC_median_analysis.xlsx', delimiter=',', header=None)
customdate = datetime.datetime(2015, 3, 18, 0)  #date start
x = [customdate + datetime.timedelta(hours=i) for i in range(len(y1))]

#plot config
fig, host = plt.subplots(figsize=(9, 4))
plt.grid(linestyle='dotted')

p1, = host.plot(x, y1, "black", label="TEC")
p2, = host.plot(x, y2, "darkorange", label="Median TEC")

host.set_xlabel("Maret 2015")
host.set_ylabel("TEC $(TECU)$")

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
