import csv
import matplotlib.pyplot as plt

csvfile = csv.reader(open('es1.csv'), delimiter=',')

# average_delay = list(map(float, next(csvfile)))
# rho = list(map(float, next(csvfile)))
# plt.figure(1)
# plt.title('Average Delay vs Rho')
# plt.plot(rho, average_delay)
# plt.xlabel(r'Utilization factor $\rho$')
# plt.ylabel('Average Delay')
# plt.grid()
# plt.tight_layout()
# plt.savefig('avg_delay_vs_rho_1.pdf')

a = list(map(float, next(csvfile)))
size = list(map(float, next(csvfile)))
plt.figure(2)
plt.title(r'Queue size vs a for $P[Overflow] = 1e-5$')
plt.bar(a, size)
plt.xlabel('Arrivals probability')
plt.ylabel('Queue size')
plt.grid()
plt.tight_layout()
plt.savefig('queue_size_vs_a.pdf')
