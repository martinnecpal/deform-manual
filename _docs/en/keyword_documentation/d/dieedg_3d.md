---
lang: en
title: "DIEEDG (3D)"
---

# DIEEDG

|  (Object data – 3D)  
---|---  
|  Last updated on : 12-08-2013  
  
* * *

DIEEDG Object, DieEdgeNo, Etype, Npoints

PointNo(1), PointNo(2), …, PointNo(Npoints)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
DieEdgeNo |  Die Edge Definition No. |  None  
Etype |  Die Edge Type =**1** : Default Edges Type |  None  
Npoints |  Number of Points in the edge |  None  
PointNo(i) |  ith Point number in the edge |   
|  |   
  
DEFINITION  
---  
DIEEDG specifies important edges on die geometry. Currently it has been used to define feature edges of die geometry for extrusion simulation. PointNo can have negative sign, which indicates that the point is located at sharp corner.  
  
RELATED TOPICS  
---  
[Geometry](/docs/en/pre_processor/12_geometry_modelling/12_geometry_modelling/), [Extrusion wizard](/docs/en/operation_templates/31_extrusion/31_introduction_to_extrusion/)
