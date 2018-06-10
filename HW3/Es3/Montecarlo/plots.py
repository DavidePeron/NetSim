import matplotlib.pyplot as plt
import csv

csvfile = csv.reader(open('geraf.csv'), delimiter=',')

D = list(map(float, next(csvfile)))
M = list(map(float, next(csvfile)))

for d in D:
    n_hops = list(map(float, next(csvfile)))
    std_dev_on_hops = list(map(float, next(csvfile)))

    plt.figure()
    geraf = plt.errorbar(M, n_hops, std_dev_on_hops, ecolor='k', elinewidth=1, capsize = 5, label='GeRaF')
    gaf_best = plt.plot(float(M[-1])/2, d*5**(.5), 'or', label='GAF best case')
    gaf_worst= plt.plot(float(M[-1])/2, d*10**(.5), 'ok', label='GAF worst case')
    plt.title('GeRaF with D = ' + str(d))
    plt.xlabel('average number of nodes in range')
    plt.ylabel('number of hops (avg +/- stdev)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig('hops_montecarlo_D=' + str(d) + '.pdf')
