import csv
import matplotlib.pyplot as plt

b = [0.33, 0.5, 0.66]
csvfile = csv.reader(open('es1.csv'), delimiter=',')
size = next(csvfile)
size = list(map(int, size))

plt.figure(1)
plt.title(r'Queue size vs b for $P[Overflow] = 1e-5$')
plt.bar(b, size)
plt.xlabel('Parameter of the geometric service time')
plt.ylabel('Queue size')
plt.grid()
plt.tight_layout()
plt.savefig('queue_size_vs_b.pdf')
