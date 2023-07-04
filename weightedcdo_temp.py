import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf
import cmocean
import datetime

ds2 = xr.open_dataset('/Users/kyra/documents/Summer23/gm.nc')
ts2 = ds2.TS
ts2.time

new = np.array(ts2).reshape(3001)
plt.plot(new)
