import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

m = 2**31
b = 1
s = 653
#LCG
a = 65539
x = []
x.append((a*s+b)%m)
start = time.time()
for i in range(0,2000):
    x.append((a*x[-1] + b)%m)

x[:] = [k/m for k in x] #Normalization of x

# fig = plt.figure(1)
# for i in range(0,len(x) - 1):
#     plt.plot(x[i],x[i+1], '.b', markersize=2)

# plt.tight_layout()
# plt.savefig('es5_a.pdf')

# print(range(11,17))

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
for i in range(0,len(x) - 2):
    ax.scatter(x[i],x[i+1], x[i+2], c='b', marker='.')
ax.view_init(azim=50)
# ax.view_init(elev=60)
plt.tight_layout()
plt.savefig('es5_b.pdf')
end = time.time()
print('Time = '+str(end - start))
