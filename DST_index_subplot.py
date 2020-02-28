import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import gridspec
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime

#initialize variables Main DST
y1 = pd.read_excel('Data/DST.xlsx')
customdate = datetime.datetime(2015, 3, 1, 0)
x1 = [customdate + datetime.timedelta(hours=i) for i in range(len(y1))]

#initialize variables Subplot DST
y2 = pd.read_excel('Data/DST_subplot.xlsx')
customdate = datetime.datetime(2015, 3, 15, 0)
x2 = [customdate + datetime.timedelta(hours=i) for i in range(len(y2))]

fig = plt.figure(figsize=(8, 5))
gs = gridspec.GridSpec(
    2,
    1,
    #	width_ratios=[1, 2],
    #	height_ratios=[2, 3]
)

#subplot main DST
ax = plt.subplot(gs[0])
formatter = mdates.DateFormatter('%d')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.plot(x1, y1, 'r', linewidth=0.75)
plt.ylabel('DST Index $(nT)$')
plt.grid(linestyle='-')

#subplot DST zoomin
ax2 = plt.subplot(gs[1])
formatter = mdates.DateFormatter('%d')
plt.gcf().axes[1].xaxis.set_major_formatter(formatter)
plt.plot(x2, y2, 'r', linewidth=0.75)
plt.xlabel('Maret 2015')
plt.ylabel('Indeks DST $(nT)$')
plt.grid(linestyle='-')

plt.show()
