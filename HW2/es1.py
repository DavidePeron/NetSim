import scipy.stats as stats
import matplotlib.pyplot as plt
from collections import deque
from pandas.tools.plotting import autocorrelation_plot

plt.close('all')

print ('Hello World!')
s = 100
a = 16807
m = 2**31 - 1
x = deque()
for i in range(0,1000):
    x.append(((s*a**i)%m)/m)

fig = plt.figure(1)
ax = fig.add_subplot(111)
stats.probplot(x, dist='uniform', plot=ax)
ax.get_lines()[0].set_marker('+')
ax.get_lines()[0].set_markersize(4.0)
ax.set_title("QQ Plot vs an uniform distribution")
plt.grid()

plt.figure(2)
autocorrelation_plot(x)

fig = plt.figure(3)
original_x = x;
for i in range(1,10):
    disp(x.rotate(100))
    ax = fig.add_subplot(3,3,i)
    plt.plot(original_x, x)
    ax.set_title("h = " + str(100*i))

plt.show()
