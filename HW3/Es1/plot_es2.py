import csv
import matplotlib.pyplot as plt

csvfile = csv.reader(open('es2.csv'), delimiter=',')

b = list(map(int, next(csvfile)))
size = list(map(int, next(csvfile)))

plt.figure(1)
plt.title(r'Queue size vs b for $P[Overflow] = 1e-5$')
plt.bar(b, size)
plt.xlabel('Parameter of the geometric service time')
plt.ylabel('Queue size')
plt.grid()
plt.tight_layout()
plt.savefig('queue_size_vs_b.pdf')
