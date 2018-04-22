
import scipy.stats as stats
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
import numpy as np
import math

plt.close('all')

s = 100
a = 16807
m = 2**31 - 1

# Figure 6.5
x = []
for i in range(0,1000):
    x.append(((s*a**i)%m)/m)

fig = plt.figure(1)
ax = fig.add_subplot(111)
stats.probplot(x, dist='uniform', plot=ax)
ax.get_lines()[0].set_marker('+')
ax.get_lines()[0].set_markersize(4.0)
ax.set_title("QQ Plot vs an uniform distribution")
plt.grid()
plt.tight_layout()
plt.savefig('fig-6_5a.pdf')

plt.figure(2)
autocorrelation_plot(x)
plt.tight_layout()
plt.savefig('fig-6_5b.pdf')

fig = plt.figure(3)
original_x = x;
for i in range(1,10):
    x = np.roll(x, 100)
    ax = fig.add_subplot(3,3,i)
    plt.plot(original_x, x, '.', markersize=1)
    ax.set_title("h = " + str(100*i))
plt.tight_layout()
plt.savefig('fig-6_5c.pdf')

#Figure 6.7
s1 = 1
s2 = 2
x1 = []
x2 = []
for i in range(0,1000):
    x1.append(((s1*a**i)%m)/m)
    x2.append(((s2*a**i)%m)/m)

fig = plt.figure(4)
plt.plot(x1, x2, '.', markersize=1)
plt.title('Two Streams, seeds = 1 and 2')
plt.tight_layout()
plt.savefig('fig-6_7a.pdf')

#Qui non riesco a mettere x2[-1] o comunque seeds < 1,s2*a**i risulta troppo grande
s2 = 568
x2 = []
print(s2*a**10)
for i in range(0,1000):
    x2.append(((s2*a**i)%m)/m)

fig = plt.figure(5)
plt.plot(x1, x2, '.', markersize=1)
plt.title('Two Streams, seeds = 1 and ' + str(s2))
plt.tight_layout()
plt.savefig('fig-6_7b.pdf')

# #Figure 6.10 (a)
np.random.seed(1)
a = 10
k = 1
dist = []
sample_dist = []
for i in range(0,2000):
    isRightDistributed = False
    while not isRightDistributed:
        u = np.random.rand()
        x = np.random.rand()*2*a - a
        f_x = k*(math.sin(x)**2)/(x**2)
        if u <= f_x:
            isRightDistributed = True
    dist.append(f_x)
    sample_dist.append(x)
fig = plt.figure(6)
plt.bar(sample_dist, dist)
plt.tight_layout()
plt.savefig('fig-6_10a.pdf')

#Figure 6.10 (b)
x_1_dist = []
x_2_dist = []
for i in range(0,20000):
    isInsideTheRectangle = False
    while not isInsideTheRectangle:
        x_1 = np.random.rand()
        x_2 = np.random.rand()
        u = np.random.rand()
        if u <= abs(x_1 - x_2):
            isInsideTheRectangle = True
    x_1_dist.append(x_1)
    x_2_dist.append(x_2)
# print(x_1_dist)
fig = plt.figure(7)
plt.plot(x_1_dist, x_2_dist, '.', markersize=1)
plt.tight_layout()
plt.savefig('fig-6_10b.pdf')
plt.close()
