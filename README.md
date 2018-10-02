# ece-postprocess
This repository contains scripts for the post-processing of the output from EC-Earth AMIP experiments.
<br />
<br />
## AMET_land_surface.py
The code aims to calculate the atmospheric meridional energy transport (AMET) based on the direct output from EC-Earth simulation. The full pipeline includes steps as follows: <br />
1.mass budget correction <br />
2.vertical integral of zonally integrated meridional energy transport <br />
<br />
More information about the implementation of the mass budget correction through the penalty on baratropic winds can be found in Trenberth's paper 'Climate Diagnostics from Global Analyses: Conservation of Mass in ECMWF Analyses'. <br>
For the calculation of meridional transport, please refer to the work by Trenberth and Caron 'Estimates of Meridional Atmosphere and Ocean Heat Transports'. <br>

Following fields are saved as netcdf files with a frequency of 3 hour: <br />
* 3 hourly U at 850, 500, 200 hPa <br />
* 3 hourly V at 850, 500, 200 hPa <br />
* 3 hourly T at 850, 500, 200 hPa <br />
* 3 hourly Z at 850, 500, 200 hPa <br />
* 3 hourly Q at 850, 500, 200 hPa <br />
* 3 hourly PT,T2M,U10M,V10M,SLHF,SP,MSL,LSP,CP,TCC,SSHF,SSR,STR,TSR,TTR,SRO <br />

Each netCDF file containing all the fields above is approximately 7.6GB per month.

In addition, the monthly mean of each component of meridional energy transport is saved as well: <br>
* monthly mean total AMET <br />
* monthly mean internal energy transport <br />
* monthly mean latent energy transport <br />
* monthly mean geopotential transport <br />
* monthly mean kinetic energy transport <br />
* monthly mean meridional baratropic wind correction <br />
* monthly mean zonal baratropic wind correction <br />

The fields above are saved as two seperate files containing spatial information and zonal integral. The netCDF files are approximately 22MB per month.

The fields above are saved through the command line tool "CDO". <br>

Please run the script in the following folder to perform the post-processing:<br>
ece-postprocess/ece_postprocess/scripts/
```
$ python ece-postprocess --rundir <path> --expname <exp>
```
The details about the arguments can be found inside the script.<br>

The output from EC-Earth must be provided with the standard name as:<br>
```
ICMGG<exp>+<time> # output on gaussian grid
ICMSH<exp>+<time> # output on spectral coordinate, must be changed to gaussian grid
```
where <exp> is the experiment name, and <time> is the time of the exp. They shoud be given as the argument. <br>

The script is recommended to be used together with the workflow manager [suite.rc](https://github.com/blue-action/ece-postprocess/blob/master/cylc/suite.rc). <br>
