import numpy as np
import matplotlib.pyplot as plt

num_rv = 3000
num_sim = 150000

rvs = []
for i in range(0, num_sim):
	rvs.append(np.exp(np.random.rand()))

rvs = np.array(rvs)
E_theta = np.sum(rvs)/num_sim
STD_theta = np.sum((rvs - E_theta)**2)/num_sim
print("E[e^u]: " + str(E_theta))
print("Sigma[e^u]: " + str(STD_theta))
rvs_anti = []
# Using antithetics variables
for i in range(0, int(num_sim/2)):
	u = np.random.rand()
	rvs_tmp = (np.exp(u) + np.exp(1-u))/2
	rvs_anti.append(rvs_tmp)

rvs_anti = np.array(rvs_anti)
E_theta_anti = 2*np.sum(rvs_anti)/num_sim
STD_theta_anti = 2*np.sum((rvs_anti - E_theta_anti)**2)/num_sim

print("Using antithetics variables: ")
print("E[e^u]: " + str(E_theta_anti))
print("Sigma[e^u]: " + str(STD_theta_anti))
x = [1, 2]
y = [STD_theta, STD_theta_anti]
y_error = [0.14*STD_theta, 0.14*STD_theta_anti]
plt.figure()
plt.errorbar(x, y, fmt='o',  yerr = y_error)
plt.xticks(x, ['Raw estimator', 'Antithetics variables'])
plt.grid()
plt.title("Variance comparison")
plt.tight_layout()
plt.savefig("antithetics.pdf")
