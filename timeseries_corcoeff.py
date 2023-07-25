import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import netCDF4 as nc
from scipy import interpolate

ice_time = np.arange(3001, 0, -1)

longitudes = [108,90,215,59]
latitudes = [119,165,104,149]

gdf = nc.Dataset('/Users/kyra/documents/Summer23/h.1000yr.shann.nc')
grid_points = gdf['h'][:]

d = []
for i in range(4):
    d.append(grid_points[:, latitudes[i], longitudes[i]])

plt.figure(figsize=(10, 3))
colors = ['#56aeff', '#de6fa1', '#b7505b', '#cc2400'] 

for i in range(4):
    slat, slon = latitudes[i], longitudes[i]
    plt.plot(ice_time, d[i]/1000, color=colors[i])

plt.xlabel('Time (Kiloyears)')
plt.xlim(3001, 0)
plt.ylabel('Ice Thickness (m)')
plt.ylim(0, 5)

plt.title('Time Series for Ice Thickness 3Ma ~')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

legend_labels = ['57W,83S', '118W,80S', '115E,75S', '97W,75S']

plt.legend(legend_labels, loc='center')
plt.show()

nd = []
for i in range(4):
    xt = grid_points[:, latitudes[i], longitudes[i]]
    masked_xt = np.ma.masked_invalid(xt)
    mean = np.mean(masked_xt)
    stdev = np.std(masked_xt)

    normalized_xt = (xt - mean) / stdev
    nd.append(normalized_xt)
    # print(f"Grid Point {i+1} - Latitude: {latitudes[i]}, Longitude: {longitudes[i]}")
    # print(f"Standard Deviation: {np.std(xt)}")
    # print(f"Normalized Value: {(d[i])}")

plt.figure(figsize=(10, 3))

for i in range(4):
    plt.plot(ice_time, nd[i], color=colors[i])

plt.xlabel('Time (Kiloyears)')
plt.xlim(3001, 0)
plt.ylabel('Ice Thickness (m)')
plt.ylim(-1, 5)

plt.title('Time Series for Normalized Ice Thickness 3Ma ~')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

legend_labels = ['57W,83S', '118W,80S', '115E,75S', '97W,75S']

plt.legend(legend_labels, loc='center')
plt.show()
