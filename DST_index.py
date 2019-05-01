import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np 
import pandas as pd 
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime

customdate = datetime.datetime(2015, 3, 1, 0)
fig = plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
ax = fig.add_subplot(111)

#initialize variables
yo = pd.read_csv('data/csvfile.csv', delimiter=',', header=None)
y = yo.values.tolist()
x = [customdate + datetime.timedelta(hours=i) for i in range(len(y))]

ymin = np.nanmin(y)
xpos = y.index(ymin)
xmin = x[xpos]

formatter = mdates.DateFormatter('%d')

#annotate
ax.annotate(ymin, xy=(xmin, ymin), xytext=(xmin, ymin-52),
            arrowprops=dict(facecolor='black', shrink=0.1, width=2.3, headwidth=8
            	,headlength=8),
            )

#plot
ax.plot(x, y, 'r', linewidth = 1)
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.xlabel('March 2015')
plt.ylabel('DST Index (nT)')
ax.set_ylim(-300,70)

plt.show()