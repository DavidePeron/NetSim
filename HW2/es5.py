import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

m = 2**31
b = 1
s = 653
#LCG1
a = 65539
x = []
x.append((a*s+b)%m)
start = time.time()
for i in range(0,25):
    x.append((a*x[-1] + b)%m)
    # for j in range(0,5):
    #     x_tmp = (a*x_tmp + b)%m
    # x.append((a*x_tmp + b)%m)
# periodReached = False
# while not periodReached:
#     x_new =  (a*x[-1] + b)%m
#     if x_new in x:
#         periodReached = True
#     else:
#         x.append(x_new)

x[:] = [k/m for k in x] #Normalization of x

# fig = plt.figure(1)
# for i in range(0,len(x)):
#     for j in range(0,len(x)):
#         plt.plot(x[i],x[j], '.', markersize=2)

# plt.tight_layout()
# plt.savefig('es5_a.pdf')

# print(range(11,17))

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
for i in range(0,len(x),3):
    for j in range(0,len(x)):
        for k in range(0,len(x)):
            # ax.scatter(x[i],x[j], x[k], s=2, c=colors[int(i%len(colors))], marker='.')
            ax.scatter(x[i],x[j], x[k], s=2, c=(1, i/len(x), 0), marker='.')
ax.view_init(azim=80)
plt.tight_layout()
plt.savefig('es5_b_80.png')
end = time.time()
print('Time = '+str(end - start))
