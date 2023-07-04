import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf
import cmocean
import datetime

#opening dataset
ds = xr.open_dataset('/Users/kyra/documents/Summer23/pCESM.3Ma_TS.1000yr.nc')
ts = ds.TS
print(ts)

#selects from ts at nearest coordinates to a longitude of 180 and latitude of 0, time from -mil
ts.sel(lon=180,lat=0,method='nearest').sel(time=slice(-1000000,0)).plot()

#selects from ts at the first time index, plots for latitudes between 40 and 90
ts.isel(time=0).sel(lat=slice(40,90)).plot()

#creating polar contour plot
plt.rcParams.update({'font.size': 7})
fig = plt.figure(num=1,figsize=(4,2), dpi=300, facecolor='w',edgecolor='k')
da_plot = ts.isel(time=0).sel(lat=slice(60,90))
ax1 = plt.subplot2grid((1,1), (0,0),
        projection=ccrs.NorthPolarStereo())

ax1.contourf(da_plot.lon,da_plot.lat,da_plot,
        transform=ccrs.PlateCarree())
ax1.coastlines()
