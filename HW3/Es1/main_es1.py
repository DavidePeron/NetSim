import simulator_es1 as sim
import numpy as np
import matplotlib.pyplot as plt
import csv

num_simulations = 3
slots_counter = 10000
a = [0.25, 0.33, 0.33]
# a = np.linspace(0.001, 1/3, num=100)

average_delay = []
rho = []

writer = csv.writer(open('es1.csv', 'a'), delimiter=',')

# # Run Simulator
# metrics = {}
# for i in a:
#     delay = 0
#     rho_tmp = 0
#     for k in range(0, num_simulations):
#         metrics[i] = sim.run_queue(slots_counter, i, limited_size = False)
#         delay += np.mean(metrics[i]['delay'])
#         rho_tmp += float(metrics[i]['busy_slots'])/slots_counter

#     average_delay.append(float(delay)/num_simulations)
#     rho.append(float(rho_tmp)/num_simulations)

# writer.writerow(average_delay)
# writer.writerow(rho)

size = []
queue_size = 1
a = sorted(a)
for i in a:
    size_found = False
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
    print('Size for a=' + str(i) + ' is ' + str(queue_size))

writer.writerow(a)
writer.writerow(size)


# # Compute statistical metrics and plot them
# average_delay = []
# for key, run in metrics.items():
#     average_delay.append(np.mean(run['delay']))

# plt.figure(1)
# plt.title('Queue size vs Time')

# for key, run in metrics.items():
#     plt.semilogy(range(0,len(run['queue_size'])), run['queue_size'], label='a = ' + str(round(key,2)))


# plt.legend(loc = 2)
# plt.xlabel('Time')
# plt.ylabel('Queue size')
# plt.grid()
# plt.tight_layout()
# plt.savefig('queue_size_vs_time_logy.pdf')

# plt.show()
