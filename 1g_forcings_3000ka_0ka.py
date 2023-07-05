import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/kyra/documents/Summer23/pCESM.3Ma_CO2_d18O_obPara.txt', delim_whitespace=True, header=None)

na = df.to_numpy()
time = na[0:3000, 0]

fig, ax = plt.subplots()
fig.subplots_adjust(right=2)

twin1 = ax.twinx()

p1, = ax.plot(time, co2, 'mediumseagreen', label="CO2", linewidth = 0.8)
p2, = twin1.plot(time, d180, 'red', label="d180 from LRO4 Records", linewidth = 0.8)

axs.set_xlabel("Time (kiloyears)")
ax.invert_xaxis()
ax.set_ylabel("CO2")
twin1.set_ylabel("d180 from LRO4 Records")
twin1.invert_yaxis()

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())

tkw = dict(size=4, width=1.5)
ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)

plt.show()

#####version with precession separate and obliquity
fig, axs = plt.subplots()
fig.subplots_adjust(right=2)

twin3 = axs.twinx()

p3, = axs.plot(time, eccentricity, 'blue', label="Eccentricity", linewidth = 1)
p4, = twin3.plot(time, obliquity, 'tab:orange', label="Obliquity", linewidth = 1)

twin4.spines.right.set_position(("axes", 1.10))

axs.set_ylabel("Eccentricity")
twin3.set_ylabel("Obliquity")

axs.set_xlabel("Time (kiloyears)")
axs.invert_xaxis()

axs.yaxis.label.set_color(p3.get_color())
twin3.yaxis.label.set_color(p4.get_color())

tkw = dict(size=4, width=1.5)
axs.tick_params(axis='y', colors=p3.get_color(), **tkw)
twin3.tick_params(axis='y', colors=p4.get_color(), **tkw)
plt.show()

##
fig, ps = plt.subplots()
fig.subplots_adjust(right=2)
p, = ps.plot(time, precession, 'purple', label="Precession", linewidth = 1, alpha=0.6)
ps.set_ylabel("Precession")
ps.yaxis.label.set_color(p.get_color())
ps.set_xlabel("Time (kiloyears)")
ps.invert_xaxis()
ps.tick_params(axis='y', colors=p.get_color(), **tkw)
plt.show()

plt.savefig('forcings_3000ka_0ka.png')
