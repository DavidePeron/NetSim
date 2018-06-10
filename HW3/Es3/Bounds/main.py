from simulator import Simulator
import numpy as np
import csv

num_simulations = 100
M = range(1, 31)
nu = 50

# Distance between Rx and Tx
D = [20]
writer = csv.writer(open('geraf_bounds.csv', 'a'), delimiter=',')
# writer.writerow(D)
# writer.writerow(M)
m_sim = Simulator()
m_sim.nu = nu

for d in D:
    m_sim.D = d
    n_hops = []
    std_dev_on_hops = []

    for m in M:
        m_sim.M = m
        n_hops_m = []
        for _ in range(num_simulations):
            n_hops_m.append(m_sim.run())

        n_hops.append(np.mean(n_hops_m))
        std_dev_on_hops.append(np.std(n_hops_m))

    writer.writerow(n_hops)
    writer.writerow(std_dev_on_hops)
