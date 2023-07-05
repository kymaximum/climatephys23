import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/kyra/documents/Summer23/pCESM.3Ma_CO2_d18O_obPara.txt', delim_whitespace=True, header=None)

na = df.to_numpy()
time = na[0:3000, 0]

ax = plt.gca()
co2 = na[0:3000, 1]
plt.plot(time, co2, linewidth = '0.75')
plt.title("CO2/kiloyears")
plt.xlabel("Time (kiloyears)")
plt.ylabel("CO2")
ax.invert_xaxis()

ax = plt.gca()
d180 = na[0:3000, 2]
plt.plot(time, d180, linewidth = '0.75')
plt.title("LR04 Benthic Stack")
plt.xlabel("Time (kiloyears)")
plt.ylabel("d180 from LRO4 Records")
ax.invert_xaxis()

ax = plt.gca()
eccentricity = na[0:3000, 3]
plt.plot(time, eccentricity, linewidth = '0.75')
plt.title("Eccentricity/kiloyears")
plt.xlabel("Time (kiloyears)")
plt.ylabel("Eccentricity")
ax.invert_xaxis()

ax = plt.gca()
obliquity = na[0:3000, 4]
plt.plot(time, obliquity,linewidth = '0.75')
plt.title("Obliquity/kiloyears")
plt.xlabel("Time (kiloyears)")
plt.ylabel("Obliquity")
ax.invert_xaxis()

ax = plt.gca()
precession = na[0:3000, 5]
plt.plot(time, precession, linewidth = '0.75')
plt.title("Precession/kiloyears")
plt.xlabel("Time (kiloyears)")
plt.ylabel("Precession")
ax.invert_xaxis()
