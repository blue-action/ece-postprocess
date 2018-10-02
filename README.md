# ece-postprocess
This repository contains scripts for the post-processing of the output from EC-Earth AMIP experiments.
<br />
<br />
## AMET_land_surface.py
The code aims to calculate the atmospheric meridional energy transport based on the output from EC-Earth simulation. This includes: <br />
1.mass budget correction <br />
2.vertical integral of zonally integrated meridional energy transport <br />
<br />
It also saves the following fields as netcdf files (3 hourly): <br />
* 6 hourly U, V, T, Z at 850, 500, 200 hPa <br />
* Q,PT,T2M,U10M,V10M,SLHF,SP,MSL,LSP,CP,TCC,SSHF,SSR,STR,TSR,TTR <br />

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

For more information about the algorithm of the mass budget correction, please refer to Trenberth, 1991.

For more information about the algorithm of the computation of meridional energy transport, please refer to Trenberth and Caron, 2001.
