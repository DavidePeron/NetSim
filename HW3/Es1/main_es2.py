import simulator_es2 as sim
import numpy as np
import matplotlib.pyplot as plt
import collections
import csv

# Configurations
slots_counter = 10000
blocking_queue = False
queue_size = 10
num_simulations = 5
b = [0.33, 0.5, 0.66]
# b = np.linspace(0.5, 0.99, num=100)

# Run Simulator
metrics = {}
average_delay = []
rho = []
#Exercise 1.a and 1.b
# for i in b:
#     delay = 0
#     rho_tmp = 0
#     for k in range(0, num_simulations):
#         metrics[i] = sim.run_queue(slots_counter, i, limited_size = blocking_queue, maximum_size = queue_size)
#         delay += np.mean(metrics[i]['delay'])
#         rho_tmp += float(metrics[i]['busy_slots'])/slots_counter
#     average_delay.append(float(delay)/num_simulations)
#     rho.append(float(rho_tmp)/num_simulations)

# Exercise 1.c
writer = csv.writer(open('es2.csv', 'w'), delimiter=',')
size = []
for i in b:
    size_found = False
    queue_size = 1
    while not size_found:
        p_overflow_tmp = 0
        for k in range(0, num_simulations):
            metrics = sim.run_queue(slots_counter, i, limited_size = True, maximum_size = queue_size)
            p_overflow_tmp += metrics['p_overflow']
        p_overflow = float(p_overflow_tmp)/num_simulations
        if(p_overflow <= 1e-5):
            size_found = True
        else:
            queue_size += 1
    size.append(queue_size)
    print('Size for b=' + str(i) + ' is ' + str(queue_size))

writer.writerow(b)
writer.writerow(size)

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

# plt.figure(2)
# plt.title('Average Delay vs b')
# plt.plot(b, average_delay)
# plt.xlabel('Parameter of the geometric service time')
# plt.ylabel('Average Delay')
# plt.grid()
# plt.tight_layout()
# plt.savefig('avg_delay_vs_b.pdf')

# plt.figure(3)
# plt.title(r'Average Delay vs $\rho$')
# plt.stem(rho, average_delay, lw=1, markersize=1)
# plt.xlabel('Utilization factor')
# plt.ylabel('Average Delay')
# plt.grid()
# plt.tight_layout()
# plt.savefig('avg_delay_vs_rho.pdf')

# plt.show()
