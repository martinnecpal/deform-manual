---
lang: sk
title: "GEOERR (2D3D)"
---

# GEOERR

|  (Simulation control)  
---|---  
_Update History:_ v11 – Contact tolerances for thermal and wear calculations have been introduced. |  Last updated on : 07-08-2013  
  
* * *

GEOERR Res, Ren,Thermal, Wear

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Res |  Relative error limit in tangential direction |  1.0 E-06  
Ren |  Relative error limit in normal direction |  1.0 E-04  
CtlTol |  Contact tolerance for thermal calculation (new in v11) |  0.0  
Wear |  Contact tolerance tool wear calculation (new in v11) |  0.0  
  
DEFINITION  
---  
GEOERR specifies the values of error limits in geometry handling.  
  
REMARKS  
---  
The DEFORM system calculates the overall geometry size, geosiz, and the absolute error limits in tangential and normal directions are determined by aes = geosiz * Res aen = geosiz * Ren Geometric lengths smaller that aes and aen are neglected. If CtlTol is specified, in addition to deformation contact, the interface heat transfer calculations are as follows: If CtlTol > 0, calculation between surface elements with normal distance less than CtlTol. If CtlTol < 0, relative tolerance will be decided based upon testing.  
  
RELATED TOPICS  
---  
Simulation Controls:[ Advanced Controls](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)\- [Error Tolerances](../../pre_processor/9_simulation_controls/9_7_advanced_options.htm#9.7.2._Error_Tolerances), [Geometry](/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/)
