import simulator as sim
import numpy as np
import matplotlib.pyplot as plt

metrics = []

lambd = np.linspace(0.1, 0.66, num=40)

for i in lambd:
	metrics.append(sim.run_queue(i))

metrics = sorted(metrics, key=lambda x: x[1])
metrics = np.array(metrics)

plt.figure()
plt.plot(metrics[:,1], metrics[:,0])
plt.xlabel("Rho")
plt.ylabel("Delay")
plt.grid()
plt.tight_layout()
plt.savefig("delay_vs_rho.pdf")
