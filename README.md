# Exploring Ice-Sheet Dynamics and Paleoclimate (Summer 2023)

**An archive of my first computational climate-science research, completed during a summer 2023 internship.**

This repository captures the beginning of my work with ice-sheet and paleoclimate model output: learning to navigate multidimensional climate data, construct time series and spatial visualizations, and ask how changes in ice thickness and ice volume relate to atmospheric CO₂, orbital forcing, and other records of past climate.

These are exploratory notebooks and scripts from an early stage of learning, rather than a polished or fully reproducible research package. I have since extended this line of inquiry with **Fourier and wavelet analyses** and studies of **variability using climate-model output**. Those later analyses are part of the broader research trajectory, **not analyses documented or implemented in this 2023 repository**.

## Scientific context

Ice sheets respond to climate forcing on a range of timescales, and their evolution contributes to global sea-level change. Paleoclimate records and model simulations offer complementary ways to investigate these relationships. This internship introduced me to handling long climate-model time series, comparing variables sampled at different resolutions, and examining how spatially heterogeneous ice-sheet behavior can be obscured by hemispheric or global averages.

The source code works with a paleoclimate forcing table spanning approximately **3 million years ago to the present** (at nominal 1-kyr spacing), alongside modeled ice thickness, ice volume, and surface temperature. Some notebooks focus on shorter windows, including approximately **3.0–2.5 Ma** and the **last ~125 kyr**. Variables include CO₂, the LR04 benthic oxygen-isotope stack (δ¹⁸O), eccentricity, obliquity, precession, and modeled ice-sheet fields.

## What is in this repository?

### 1. Paleoclimate forcing and temperature time series

- [`trial_sevgraphs_forcing.py`](trial_sevgraphs_forcing.py) and [`1g_forcings_3000ka_0ka.py`](1g_forcings_3000ka_0ka.py): early plots of CO₂, δ¹⁸O, and orbital parameters across the forcing record.
- [`avgtemperature_mean.py`](avgtemperature_mean.py): inspection of model surface temperature (`TS`), including point time series and a North Polar stereographic map.
- [`weightedcdo_temp.py`](weightedcdo_temp.py): exploratory plotting of a previously processed global-mean temperature series.
- [`extforcing125.py`](extforcing125.py) and [`summarygraph.ipynb`](summarygraph.ipynb): multi-panel comparisons of forcing, temperature, and ice-volume-derived sea-level-equivalent series, particularly over the last ~125 kyr.

### 2. Ice volume and sea-level equivalent

- [`sealevel_ice_volume.py`](sealevel_ice_volume.py): an introductory conversion from an ice-volume change estimate to sea-level equivalent.
- [`shout_plotting.py`](shout_plotting.py) and [`nhout_plotting.py`](nhout_plotting.py): exploratory Southern and Northern Hemisphere ice-volume series.
- [`extforcing125.py`](extforcing125.py) and [`summarygraph.ipynb`](summarygraph.ipynb): comparisons of hemispheric contributions and an attempted combined sea-level-equivalent series.

These calculations use assumed reference volumes, density factors, and ocean area. They should be treated as *exploratory conversions*, not validated sea-level reconstructions; input units and reference choices require checking.

### 3. Comparing ice behavior with climate forcing

- [`timeseriescheck.ipynb`](timeseriescheck.ipynb): interpolating forcing variables onto an ice-model time grid and plotting aligned time series.
- [`scatterplot.ipynb`](scatterplot.ipynb): scatterplots and Pearson correlations comparing ice volume with CO₂, δ¹⁸O, and orbital variables.
- [`summarygraph.ipynb`](summarygraph.ipynb): side-by-side time-series summaries to help inspect co-variation.

These correlations are descriptive and do not establish causality; in particular, temporal autocorrelation and shared long-term trends are not accounted for by a simple Pearson coefficient.

### 4. Spatial variability in ice thickness

- [`timeseries_corcoeff.py`](timeseries_corcoeff.py): raw and standardized ice-thickness time series at selected grid locations.
- [`3mastdev.ipynb`](3mastdev.ipynb): grid-cell standard deviation of modeled ice thickness over an early-Pleistocene interval.
- [`3macorrcoef.ipynb`](3macorrcoef.ipynb): grid-cell correlations between ice thickness and an interpolated CO₂ series over approximately 3.0–2.5 Ma.
- [`125corrcoef.ipynb`](125corrcoef.ipynb): standard-deviation mapping and ice-thickness/CO₂ correlation mapping for a shorter, approximately 125-kyr experiment.
- [`stdev_comparison.ipynb`](stdev_comparison.ipynb): comparison of spatial standard-deviation maps from two time windows.
- [`secondtry.ipynb`](secondtry.ipynb): preliminary experiments with spatial variability and correlation calculations.
- [`spatialpatterns_nh_sh.ipynb`](spatialpatterns_nh_sh.ipynb): exploratory notebook on Northern and Southern Hemisphere spatial patterns.

This stage was especially important for moving from individual time series to the idea that *where* ice thickness varies matters as much as how much an aggregate ice-volume curve changes.

## How the work developed

| Stage | Focus | Research skill |
| --- | --- | --- |
| Initial exploration | Climate forcings, temperature maps, and ice-volume plots | Reading model output and visualizing geophysical variables |
| Time-series comparisons | Ice volume versus CO₂, δ¹⁸O, and orbital forcing | Interpolation, alignment, scatterplots, and correlations |
| Spatial analysis | Ice-thickness standard deviations and grid-cell correlations | Working across time and space in gridded model output |
| Subsequent research (not included here) | Fourier analysis, wavelet analysis, and climate-model variability | Examining timescales, evolving periodicities, and variability beyond simple correlations |

The later work builds on questions raised here: how much ice-sheet variability is associated with different timescales, whether those relationships remain stable through time, and how spatial patterns interact with climate forcing. This repository documents **the starting point**, not the full extent of that subsequent work.

## Data and technical notes

The files refer to local research datasets, generally under `/Users/kyra/documents/Summer23/`. **Those source data files are not distributed with this repository.** The code refers to:

- a paleoclimate forcing table (`pCESM.3Ma_CO2_d18O_obPara.txt`);
- NetCDF climate-model temperature and ice-volume outputs, including `TS`, `toti`, and `h` variables;
- grid-coordinate files used to display spatial fields;
- preprocessed Northern and Southern Hemisphere model outputs.

The original environment uses Python with packages such as `numpy`, `pandas`, `matplotlib`, `xarray`, `netCDF4`, `scipy`, `cartopy`, `cmocean`, and `seaborn`; some notebooks also import `pyproj`. The scripts do not define a pinned environment or a turnkey execution order.

### Reproducibility and limitations

This is a **historical research archive**. Most scripts need input paths replaced with locally available datasets before they can run. Some also contain incomplete or experimental code, inconsistent time axes or labels, and calculations that need unit and shape checks. Figures in saved notebooks are not a substitute for re-running the analyses on verified inputs. No claim of independent validation or full reproducibility is made.

A modern replication would begin by identifying and documenting the model experiments and dataset provenance, confirming units and calendars, aligning sampling intervals explicitly, masking missing or non-ice grid cells appropriately, and validating the sea-level-equivalent conversions and spatial statistics. Trend, autocorrelation, and effective sample size would also need consideration when interpreting correlations.

## Why I keep this repository public

This was my first sustained encounter with the practical complexity of ice-sheet data. The scripts are not elegant, and some represent attempts that did not fully work. But they show the development of the questions and skills that shaped my later research: moving from simply plotting a climate variable toward understanding its variability across **space, time, and frequency**.

**Project period:** Summer 2023  
**Status:** Archived exploratory internship work; later research is not included here.
