import simulator as sim
import numpy as np
import csv

num_simulations = 500
M = range(1, 31)

# Distance between Rx and Tx
# D = [5, 10, 20]
D = [5, 10, 20]
writer = csv.writer(open('geraf.csv', 'w'), delimiter=',')
writer.writerow(D)
writer.writerow(M)

for d in D:
    n_hops = []
    std_dev_on_hops = []

    for m in M:
        n_hops_m = []
        for _ in range(num_simulations):
            n_hops_m.append(sim.run(d, m))

        n_hops.append(np.mean(n_hops_m))
        std_dev_on_hops.append(np.std(n_hops_m))

    writer.writerow(n_hops)
    writer.writerow(std_dev_on_hops)
