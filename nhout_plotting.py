#same as shout code except file path name is different

import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf
import cmocean
import datetime
import seaborn as sns

ts = xr.open_dataset('/Users/kyra/documents/Summer23/nhout/totimerged.nc')
ts = ts.toti
print(ts)
change = -ts + (26.5 * 10**6)
ice_mass = (0.9167) * change
sle = ((ice_mass * (1/361.8*(10**12))))

plt.rcParams.update({'font.size': 3})
fig = plt.figure(num=1,figsize=(4,2), dpi=300, facecolor='w',edgecolor='k')
plt.subplot(2, 2, 1)
plt.plot(sle)
plt.title("using toti data")
plt.xlabel('Mass of Ice(Gt)')
plt.ylabel('Change in Sea Level (m)')
plt.show()
