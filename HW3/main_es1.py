import simulator_es1 as sim
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

slots_counter = 10000
a = [0.25, 0.33, 0.5]
# a = np.linspace(0.001, 1/3, num=100)

# Run Simulator
metrics = {}
for i in a:
    metrics[i] = sim.run_queue(slots_counter, i)

# Compute statistical metrics and plot them
average_delay = []
for key, run in metrics.items():
    average_delay.append(np.mean(run['delay']))

plt.figure(1)
plt.title('Queue size vs Time')

for key, run in metrics.items():
    plt.semilogy(range(0,len(run['queue_size'])), run['queue_size'], label='a = ' + str(round(key,2)))


plt.legend(loc = 2)
plt.xlabel('Time')
plt.ylabel('Queue size')
plt.grid()
plt.tight_layout()
plt.savefig('queue_size_vs_time_logy.pdf')

# plt.figure(2)
# plt.title('Average Delay vs a')
# plt.plot(a, average_delay)
# plt.xlabel('Probability of arrivals')
# plt.ylabel('Average Delay')
# plt.grid()
# plt.tight_layout()
# plt.savefig('avg_delay_vs_a.pdf')

# plt.show()
