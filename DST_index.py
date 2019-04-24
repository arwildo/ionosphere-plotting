import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

plt.figure(figsize=(8, 5))

x = np.linspace(1, 31, 744)
y = np.arange(1,745)

plt.plot(x, y, 'b')
plt.xlabel('March 2015')
plt.ylabel('DST Index (nT)')

plt.show()