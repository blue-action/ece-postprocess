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
* Surface runoff                        [m] <br />
* Sub-surface runoff                    [m] <br />
* Snow albedo                           [0-1] <br />
* Snow density                          [kg/m3] <br />
* Volumetric soil water layer 1         [m3/m3] <br />
* Volumetric soil water layer 2         [m3/m3] <br />
* Volumetric soil water layer 3         [m3/m3] <br />
* Volumetric soil water layer 4         [m3/m3] <br />
* Soil temperature level 1              [K] <br />
* Snow depth                            [m] <br />
* Soil temperature level 2              [K] <br />
* Soil temperature level 3              [K] <br />
* Soil temperature level 4              [K] <br />

It needs two input parameters:<br />
* time (eg. 197901)<br />
* input and output path<br />

where time is obtained by sys.stdin.readline(), thus the script will be executed through: <br />
```
$ python AMET_land_surface.py < input_time.txt
```
The input and output path shall be specified inside the script (in the input zone). <br />

The output from EC-Earth must have the standard name with the format as:
```
ICMGGECE3+197901 # output on gaussian grid
ICMSHECE3+197901 # output on spectral coordinate, must be changed to gaussian grid
```
The script is recommended to be used together with the scheduler [job_scheduler.sh](https://github.com/blue-action/ece-postprocess/blob/master/job_scheduler.sh).

## job_scheduler.sh
This bash script aim to schedule and execute job for the post-processing of EC-Earth output on Cartesius.
