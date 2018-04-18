import numpy as np
import math
import time

lambda_par = 5
#CDF Inversion
n_vars = 10000
mean_CDF = 0
start = time.time()
for k in range(0,n_vars):
    u = np.random.rand()
    i = 0
    p = math.exp(-lambda_par)
    F = p
    while u >= F:
        p *= lambda_par/(i+1)
        F += p
        i += 1
    mean_CDF += i

mean_CDF /= n_vars
end = time.time()
time_CDF = end - start
print('CDF Time elapsed: ' + str(time_CDF) + ' Mean: ' + str(mean_CDF))

#Sum of exponentials
mean_exp = 0
start = time.time()
for i in range(0,n_vars):
    n_exp = 0
    sum = 0
    while sum <= 1:
        sum += -math.log(np.random.rand())/lambda_par
        n_exp += 1
    mean_exp += n_exp - 1

mean_exp /= n_vars
end = time.time()
time_exp = end - start
print('Exp Time elapsed: ' + str(time_exp) + ' Mean: ' + str(mean_exp))

mean_unif = 0
start = time.time()
for i in range(0,n_vars):
    rv = 1
    count = 0
    while rv > math.exp(-lambda_par):
        rv *= np.random.rand()
        count += 1
    mean_unif += count - 1

mean_unif /= n_vars
end = time.time()
time_unif = end - start
print('Uniform Time elapsed: ' + str(time_unif) + ' Mean: ' + str(mean_unif))
