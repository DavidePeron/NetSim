import numpy as np
from simulator import Simulator
import pandas as pd

# writer = csv.writer(open('results.csv', 'w'), delimiter=',')

alpha = np.linspace(0.01, 0.99, num=10)
df = pd.DataFrame(alpha, columns=["Alpha"])

threshold = [6, 10] #dB
reuse_factor = [1, 3, 4, 7]
sigma = 8 #dB
sigma_linear = 10**(float(sigma)/10)
R = 1 # radius of the approximating circle for the intended cell

sim = Simulator()
sim.sigma = sigma_linear
sim.num_sim = 1500

for rf in reuse_factor:
    sim.rf = rf
    for b in threshold:
        sim.b = b
        outage = np.array([])
        for a in alpha:
            sim.alpha = a
            outage = np.append(outage, sim.get_outage())
        df["rf" + str(rf) + "b" + str(b)] = pd.Series(outage)
df.to_csv("outage.csv", index=False)
# Capture probabilities
n = np.arange(2,31)
sim.rf = 4
sim.eta = 4

df = pd.DataFrame(n, columns=["n"])

for b in threshold:
    sim.b = b
    capture = np.array([])
    for i in n:
        capture = np.append(capture, sim.get_capture(i))
    df["b" + str(b)] = pd.Series(capture)

df.to_csv("capture.csv", index=False)
