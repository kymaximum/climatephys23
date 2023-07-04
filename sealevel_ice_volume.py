import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf
import cmocean
import datetime
import seaborn as sns

ds = xr.open_dataset('/Users/kyra/documents/Summer23/fort.92.nc')
ts = ds.toti
change = -ts + (26.5 * 10**6)
ice_mass = (0.9167) * change
sle = ((ice_mass * (1/361.8*(10**12))))

plt.rcParams.update({'font.size': 7})
fig = plt.figure(num=1,figsize=(4,2), dpi=300, facecolor='w',edgecolor='k')

plt.xlabel('Mass of Ice(Gt)')
plt.ylabel('Change in Sea Level (m)')

plt.plot(sle)
plt.grid(True)
