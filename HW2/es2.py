import pandas as pd
import numpy as np
import time

n_rvs = 10000
np.random.seed(39788)
##Generate Binomial Distribution in 3 different ways

n = 50
theta = 0.5
mean_geometric = 0
mean_bernoulli = 0
mean_CDF = 0

# Using Geometric Distribution

start = time.time()
for i in range(0,n_rvs):
    isFinished = False
    X_geometric = 0
    count = 0
    while not isFinished:
        u = np.random.rand()
        X_geometric += np.floor(np.log(u)/np.log(1-theta)) + 1
        if X_geometric >= n :
            isFinished = True
        if X_geometric <= n:
            count += 1
    mean_geometric += count
end = time.time()
time_geometric = end - start
print('GEOMETRIC Time elapsed: ' + str(time_geometric) + ' Mean: ' + str(mean_geometric/n_rvs))

# Drawing n Bernoulli rvs
start = time.time()

for i in range(0,n_rvs):
    X_bernoulli = 0
    for i in range(0,50):
        u = np.random.rand()
        if u > 0.5: #Success
            X_bernoulli += 1
    mean_bernoulli += X_bernoulli
end = time.time()
time_bernoulli = end - start
print('BERNOULLI Time elapsed: ' + str(time_bernoulli) + ' Mean: ' + str(mean_bernoulli/n_rvs))

# With CDF inversion

start = time.time()
c = theta/(1-theta)
for i in range(0,n_rvs):
    pr = (1-theta)**n
    u = np.random.rand()
    i = 0
    F = pr
    while u >= F:
        pr *= c*(n-i)/(i+1)
        F += pr
        i += 1
    X_CDF = i
    mean_CDF += X_CDF
end = time.time()
time_CDF = end - start
print('CDF Time elapsed: ' + str(time_CDF) + ' Mean: ' + str(mean_CDF/n_rvs))
