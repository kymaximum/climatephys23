import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf
import cmocean
import datetime
import seaborn as sns

df = pd.read_csv('/Users/kyra/documents/Summer23/pCESM.3Ma_CO2_d18O_obPara.txt', delim_whitespace=True, header=None)

df.head()

na = df.to_numpy()
time = na[2875:3000, 0]
co2 = na[2875:3000, 1]
d180 = na[2875:3000, 2]
eccentricity = na[2875:3000, 3]
obliquity = na[2875:3000, 4]
precession = na[2875:3000, 5]

ts = xr.open_dataset('/Users/kyra/documents/Summer23/shout/totimerge.nc')
ts = ts.toti
change = -ts + (26.5 * 10**15)
ice_mass = (0.9167) * change
sle = (ice_mass * (1/(361.8*(10**12))))
print(sle)
sle = np.array(sle).reshape(1250)

ts2 = xr.open_dataset('/Users/kyra/documents/Summer23/nhout/totimerged.nc')
ts2 = ts2.toti
#print(ts2)
change2 = -ts2 + (2.9 * 10**15)
ice_mass2 = (0.9167) * change2
sle2 = ((ice_mass2 * (1/(361.8*(10**12)))))
print(sle2)
new_sle2 = np.array(sle2).reshape(1250)
new_sle2 += sle

print(new_sle2)

ts_time = ts.time
#print(ts)
print(ts_time)
sle_time = np.array(ts_time).reshape(1250)

ts2_time = ts2.time
#print(ts)
print(ts2_time)
sle2_time = np.array(ts2_time).reshape(1250)
sle2_time += sle_time

####CO2 and d180 from LRO4 Records####
fig, ax = plt.subplots()

twin1 = ax.twinx()

p1, = ax.plot(time, co2, 'mediumseagreen', label="CO2", linewidth = 0.8)
p2, = twin1.plot(time, d180, 'red', label="d180 from LRO4 Records", linewidth = 0.8)

ax.set_xlabel("Time (kiloyears)")
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

###Precession and Eccentricity####
fig, axs = plt.subplots()

twin4 = axs.twinx()

p5, = twin4.plot(time, precession, 'tab:orange', label="Precession", linewidth = 1)
p3, = axs.plot(time, eccentricity, 'blue', label="Eccentricity", linewidth = 1)

axs.set_ylabel("Eccentricity")
twin4.set_ylabel("Precession")

axs.yaxis.label.set_color(p3.get_color())
twin4.yaxis.label.set_color(p5.get_color())

tkw = dict(size=4, width=1.5)
axs.tick_params(axis='y', colors=p3.get_color(), **tkw)
twin4.tick_params(axis='y', colors=p5.get_color(), **tkw)
axs.invert_xaxis()

plt.show()

####Sea Level Equivalent####
sle = np.array(sle).reshape(1250)
fig, ax = plt.subplots()

ax.invert_xaxis()

plt.xlabel('Time (years)')
plt.ylabel('Change in Sea Level (m): Sea Level Equivalent')
plt.rcParams.update({'font.size': 9})

line1, = plt.plot(ts_time, sle, label='Southern Hemisphere', color='blue')
line2, = plt.plot(ts2_time, sle2, label='Northern Hemisphere', color='magenta')
line3, = plt.plot(ts2_time, new_sle2,label='Overall', color='black')
leg = plt.legend(loc='upper center')

plt.show()

####Global Mean Temp####
ds = xr.open_dataset('/Users/kyra/documents/Summer23/gm.nc')
ts = ds.TS

fig, ax = plt.subplots()

ts = np.array(ts).reshape(3001)
time = []

for i in range(125):
    time.append(i)

ts = ts[0:125]

time = np.flip(time)
p1, = ax.plot(time, ts, 'indigo', label="Global Average Surface Temperature", linewidth = 0.8)
ax.invert_xaxis()
ax.set_xlabel("Time (kiloyears)")
ax.set_ylabel("Global Average Surface Temperature")

ax.yaxis.label.set_color(p1.get_color())
tkw = dict(size=4, width=1.5)
ax.tick_params(axis='y', colors=p1.get_color(), **tkw)

plt.show()
