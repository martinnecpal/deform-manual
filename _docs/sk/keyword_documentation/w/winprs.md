---
lang: sk
title: "WINPRS (2D)"
---

# WINPRS

|  (Object data - 2D)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

WINPRS Object, Iwin, Ndata, Ptype, Ttype, SpdType

Velx, Vely

Iwin(1)…Iwin(Ndata)

Followed by Data

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Iwin |  Pressure window index |  None  
Ndata |  Number of data pairs for window coord. |  None  
Ptype |  Type of pressure definition  =**0** Constant =**1** Function of time |  None  
Ttype |  Type of traction definition =**0** Constant  =**1** Function of time |  None  
SpdType |  Speed type =**1** Constant  =**2** Function of time =**-n** Following object n |  0  
  
DEFINITION  
---  
WINPRS specifies the pressure window for an object. The keyword should be used if the boundary condition of pressure is different at a specific region than the rest of the object.  
  
RELATED TOPICS  
---  
Boundary Constraints: [Deformation](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/) \- [Pressure windows](../../pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions.htm#14.2.2._Pressure_BCC) Keywords: [PRZ (2D)](/docs/sk/keyword_documentation/p/prz/), [PRZ (3D)](/docs/sk/keyword_documentation/p/prz_3d/), [LOCDEF (2D)](/docs/sk/keyword_documentation/l/locdef/), [LOCDEF (3D)](/docs/sk/keyword_documentation/l/locdef_3d/)
