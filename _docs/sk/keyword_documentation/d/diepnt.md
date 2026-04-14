---
lang: sk
title: "DIEPNT (3D)"
---

# DIEPNT

|  (Object data – 3D)  
---|---  
|  Last updated on : 27-09-2023  
  
* * *

DIEPNT Object, DiePntNo, Ptype, Npoints, BearingSurfID  
Point(1), X(1), Y(1), Z(1), LenScale(1), FricScale(1)  
: : : : : :  
Point(Npoints), X(Npoints), Y(Npoints), Z(Npoints), LenScale(Npoints), FricScale(Npoints)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
DiePntNo |  Die Point Definition No. |  None  
**Ptype** |  **Die Point Type** =**1** Bearing surface control points (length reduction) - Obsolete  
= **2** Bearing surface control points (length scale) – New from v12**** |   
Npoints |  Number of Points |  None  
BearingSurfID |  Bearing Surface ID |  0  
Point(i) |  Point number of ith data point |   
X(i) |  X coordinate of ith data point |   
Y(i) |  Y coordinate of ith data point |   
Z(i) |  Z coordinate of ith data point |   
LenScale(i) |  Bearing surface length scale (when Ptype = 2) or   
Length reduction (when Ptype = 1) of ith data point  |   
FricScale(i) |  Friction scaling factor of ith data point |   
  
DEFINITION  
---  
DIEPNT specifies important points on die geometry.   
Bearing surface control points (when Ptype 1, 2) can be defined on the entrance edges of bearing surface to control bearing suaface for extrusion simulation.  
  
  
RELATED TOPICS  
---  
[Geometry](/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/), [Extrusion wizard](/docs/sk/operation_templates/31_extrusion/31_introduction_to_extrusion/)
