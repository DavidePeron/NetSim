import simulator_es2 as sim
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

slots_counter = 10000
# b = [1/3, 1/2, 2/3]
b = np.linspace(0.5, 0.99, num=200)

# Run Simulator
metrics = {}
for i in b:
    metrics[i] = sim.run_queue(slots_counter, i)

# Compute statistical metrics and plot them
average_delay = []
rho = []
for key, run in metrics.items():
    average_delay.append(np.mean(run['delay']))
    rho.append(run['busy_slots']/slots_counter)

# plt.figure(1)
# plt.title('Queue size vs Time')

# for key, run in metrics.items():
#     plt.plot(range(0,len(run['queue_size'])), run['queue_size'], label='b = ' + str(round(key,2)), linewidth=.5)


# plt.legend(loc = 2)
# plt.xlabel('Time')
# plt.ylabel('Queue size')
# plt.grid()
# plt.tight_layout()
# plt.savefig('queue_size_vs_time_logy_es2.pdf')

plt.figure(2)
plt.title('Average Delay vs b')
plt.plot(b, average_delay)
plt.xlabel('Parameter of the geometric service time')
plt.ylabel('Average Delay')
plt.grid()
plt.tight_layout()
plt.savefig('avg_delay_vs_b.pdf')

plt.figure(3)
plt.title(r'Average Delay vs $\rho$')
plt.plot(sorted(rho), average_delay)
plt.xlabel('Utilization factor')
plt.ylabel('Average Delay')
plt.grid()
plt.tight_layout()
plt.savefig('avg_delay_vs_rho.pdf')
# plt.show()
