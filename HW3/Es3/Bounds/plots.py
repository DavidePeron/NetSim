import matplotlib.pyplot as plt
import csv

csvfile_simulation = csv.reader(open('geraf.csv'), delimiter=',')
csvfile_bounds = csv.reader(open('geraf_bounds.csv'), delimiter=',')

D = list(map(float, next(csvfile_simulation)))
M = list(map(float, next(csvfile_simulation)))
D = list(map(float, next(csvfile_bounds)))
M = list(map(float, next(csvfile_bounds)))

for d in D:
    n_hops_sim = list(map(float, next(csvfile_simulation)))
    std_dev_on_hops = list(map(float, next(csvfile_simulation)))
    n_hops_lbound = list(map(float, next(csvfile_bounds)))
    std_dev_on_hops = list(map(float, next(csvfile_bounds)))
    n_hops_ubound = list(map(float, next(csvfile_bounds)))
    std_dev_on_hops = list(map(float, next(csvfile_bounds)))

    plt.figure()
    geraf_sim = plt.plot(M, n_hops_sim, 'k^', linewidth=1, label='GeRaF - simulation')
    geraf_lbound = plt.plot(M, n_hops_lbound, '--k', linewidth=1, label='GeRaF - lower bound')
    geraf_ubound = plt.plot(M, n_hops_ubound, '-k', linewidth=1, label='GeRaF - upper bound')
    gaf_best = plt.plot(float(M[-1])/2, d*5**(.5), 'or', label='GAF best case')
    gaf_worst= plt.plot(float(M[-1])/2, d*10**(.5), 'ok', label='GAF worst case')
    plt.title('GeRaF with D = ' + str(d))
    plt.xlabel('average number of nodes in range')
    plt.ylabel('number of hops (avg +/- stdev)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig('hops_bounds_D=' + str(d) + '.pdf')
