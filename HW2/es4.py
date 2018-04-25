import numpy as np
import matplotlib.pyplot as plt

m = 101
b = 1
s = 1
#LCG1
a = 18
x = []
x.append((a*s+b)%m)
periodReached = False
while not periodReached:
    x_new =  (a*x[-1] + b)%m
    if x_new in x:
        periodReached = True
    else:
        x.append(x_new)

x[:] = [k/m for k in x] #Normalization of x
print('Period of LCG1 is ' + str(len(x)) + '\n')
if len(x) < m:
    print('LCG1 is not full period')
elif len(x) == m:
    print('LCG1 is full period')

fig = plt.figure(1)
for i in range(0,len(x)-1):
    plt.plot(x[i],x[i+1], '.b', markersize=2)
#     for j in range(0,len(x)):
#         plt.plot(x[i],x[j], '.', markersize=2)

plt.tight_layout()
plt.savefig('es4_a.pdf')

#LCG2
a = 2
x2 = []
x2.append((a*s+b)%m)
periodReached = False
while not periodReached:
    x_new =  (a*x2[-1] + b)%m
    if x_new in x2:
        periodReached = True
    else:
        x2.append(x_new)

x2[:] = [k/m for k in x2] #Normalization of x2
print('Period of LCG2 is ' + str(len(x2)) + '\n')
if len(x2) < m:
    print('LCG2 is not full period')
elif len(x2) == m:
    print('LCG2 is full period')

fig = plt.figure(2)
for i in range(0,len(x2) - 1):
        plt.plot(x2[i],x2[i+1], '.b', markersize=2)
    # for j in range(0,len(x2)):
    #     plt.plot(x2[i],x2[j], '.', markersize=2)

plt.tight_layout()
plt.savefig('es4_b.pdf')
