---
lang: sk
title: "ECPRES (2D)"
---

# ECPRES

|  (Object Data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECPRES Object, Ndata, DefPressure

Num(1), node1(i) node2(i) NorPressure(1)

: : :

Num(Ndata), node1(NData) node2(NData) NorPressure(NData)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of edge/constraint data sets |  None  
DefPressure |  Default value of normal pressure of all edges not listed in the edge constraint data sets with deformation boundary constraint code 2 |  0  
node1(i) |  1st node defining edge i |   
node2(i) |  2nd node defining edge i |   
NorPressure |  Normal Pressure |  None  
Num(i) |  Edge number |  None  
  
DEFINITION  
---  
ECPRES maintains a specified normal pressure across the face of the elements lying on the selected edge. Note that tangential pressures are no longer supported in this definition.  
  
REMARKS  
---  
Pressure is defined as force per unit area. The pressure is assumed to be linear between adjacent edges. The pressure constraint will be applied to the element faces lying between the selected boundary nodes. The pressure direction may be specified as normal. Positive normal pressure applies tension to the element faces. If no value is specified for DefPressure, it is assumed to be zero. Nodal pressure may be specified as a function of time with keyword ECDEFN.  
  
RELATED TOPICS  
---  
Object Edge data: Deformation, Boundary Constraints: Deformation -Pressure Keywords: [ECDEFN (2D)](/docs/sk/keyword_documentation/e/ecdefn/), [ECDEFN (3D)](/docs/sk/keyword_documentation/e/ecdefn_3d/), [ECCDEF (2D)](/docs/sk/keyword_documentation/e/eccdef/), [ECCDEF (3D)](/docs/sk/keyword_documentation/e/eccdef_3d/), [LOCDEF (2D)](/docs/sk/keyword_documentation/l/locdef/), [LOCDEF (3D)](/docs/sk/keyword_documentation/l/locdef_3d/)
