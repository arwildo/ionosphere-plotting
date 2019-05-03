import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np 
import pandas as pd 
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime

customdate = datetime.datetime(2015, 3, 1, 0)

#initialize variables
yo = pd.read_csv('ionosphere/ionosphere-plotting/data/DST.csv', delimiter=',', header=None)
y = yo.values.tolist()
x = [customdate + datetime.timedelta(hours=i) for i in range(len(y))]

'''
def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)
'''

fig, host = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
par2.spines["right"].set_position(("axes", 1.2))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
#make_patch_spines_invisible(par2)
# Second, show the right spine.
par2.spines["right"].set_visible(True)

p1, = host.plot(x, y, "b-", label="foF2")
p2, = par1.plot(x, y, "r-", label="Dst Indeks")
p3, = par2.plot(x, y, "g-", label="TEC")


host.set_xlabel("March 2015")
host.set_ylabel("foF2 $(Mhz)$")
par1.set_ylabel("Dst Indeks $(nT)$")
par2.set_ylabel("TEC $(TECU)$")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2, p3]

host.legend(lines, [l.get_label() for l in lines])

plt.show()