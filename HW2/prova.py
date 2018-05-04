import numpy as np
import matplotlib.pyplot as plt
import math

x = range(0, 1000)
y = [math.sin(x_i) for x_i in x]

plt.plot(x,y)

plt.show()
