import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import gridspec
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime

#initialize variables Main foF2
y1 = pd.read_excel('Data/TEC.xlsx')
customdate = datetime.datetime(2015, 3, 1, 0)
x1 = [customdate + datetime.timedelta(hours=i) for i in range(len(y1))]

#initialize variables Subplot foF2
y2 = pd.read_excel('Data/TEC_subplot.xlsx')
customdate = datetime.datetime(2015, 3, 15, 0)
x2 = [customdate + datetime.timedelta(hours=i) for i in range(len(y2))]

fig = plt.figure(figsize=(8, 5))
gs = gridspec.GridSpec(
    2,
    1,
    #	width_ratios=[1, 2],
    height_ratios=[2, 3])

#subplot main foF2
ax = plt.subplot(gs[0])
formatter = mdates.DateFormatter('%d')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.plot(x1, y1, 'black', linewidth=0.75)
plt.ylabel('TEC $(TECU)$')
plt.grid(linestyle='dotted')

#subplot foF2 zoomin
ax2 = plt.subplot(gs[1])
formatter = mdates.DateFormatter('%d')
plt.gcf().axes[1].xaxis.set_major_formatter(formatter)
plt.plot(x2, y2, 'black', linewidth=0.75)
plt.xlabel('March 2015')
plt.ylabel('TEC $(TECU)$')
plt.grid(linestyle='dotted')

plt.show()