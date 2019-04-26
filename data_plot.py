import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

times = pd.date_range('2015-10-06', periods=500, freq='10min')

fig, ax = plt.subplots(1)
fig.autofmt_xdate()
plt.plot(times, range(times.size))

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)

plt.show()