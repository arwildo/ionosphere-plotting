import matplotlib.pyplot as plt 
import numpy as np 

plt.figure(figsize = (5, 5))

plt.subplot(2, 1, 1)
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 32]
x2 = np.arange(1, 6)
y2 = x2 * np.pi
plt.plot(x, y, 'b',  x2, y2, 'r')

plt.ylabel('Sumbu Y')
plt.title('Graph')
plt.subplot(2, 1, 2)
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 32]
x2 = np.arange(1, 6)
y2 = x2 * np.pi
plt.plot(x, y, 'b',  x2, y2, 'r')

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.show()