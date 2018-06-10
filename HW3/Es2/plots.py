import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("outage.csv")

fig, axes = plt.subplots(nrows=2, ncols=2)
df.plot(x="Alpha", y="rf1b6", ax=axes[0,0])
df.plot(x="Alpha", y="rf1b10", ax=axes[0,0], grid=True, ylim=[0,1], title="Reuse Factor = 1")

df.plot(x="Alpha", y="rf3b6", ax=axes[0,1])
df.plot(x="Alpha", y="rf3b10", ax=axes[0,1], grid=True, ylim=[0,1], title="Reuse Factor = 3")

df.plot(x="Alpha", y="rf4b6", ax=axes[1,0])
df.plot(x="Alpha", y="rf4b10", ax=axes[1,0], grid=True, ylim=[0,1], title="Reuse Factor = 4")

df.plot(x="Alpha", y="rf7b6", ax=axes[1,1])
df.plot(x="Alpha", y="rf7b10", ax=axes[1,1], grid=True, ylim=[0,1], title="Reuse Factor = 7")

plt.tight_layout()
plt.savefig('outage_montecarlo.pdf')


df = pd.read_csv("capture.csv")
df.plot(x="n", y=["b6", "b10"], grid=True, title="Capture probability")
plt.tight_layout()
plt.savefig('capture_montecarlo.pdf')
