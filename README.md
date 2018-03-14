# ece-postprocess
This repository contains scripts for the post-processing of the output from EC-Earth AMIP experiments.
<br />
<br />
# AMET_land_surface.py
The code aims to calculate the atmospheric meridional energy transport based on the output from EC-Earth simulation. This includes: <br />
1.mass budget correction <br />
2.vertical integral of zonally integrated meridional energy transport <br />

It also saves the following fields as netcdf files (3 hourly): <br />
                  Surface runoff                        [m] <br />
                  Sub-surface runoff                    [m] <br />
                  Snow albedo                           [0-1] <br />
                  Snow density                          [kg/m3] <br />
                  Volumetric soil water layer 1         [m3/m3] <br />
                  Volumetric soil water layer 2         [m3/m3] <br />
                  Volumetric soil water layer 3         [m3/m3] <br />
                  Volumetric soil water layer 4         [m3/m3] <br />
                  Soil temperature level 1              [K] <br />
                  Snow depth                            [m] <br />
                  Soil temperature level 2              [K] <br />
                  Soil temperature level 3              [K] <br />
                  Soil temperature level 4              [K] <br />
