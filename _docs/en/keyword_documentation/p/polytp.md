---
lang: en
title: "POLYTP (3D)"
---

# POLYTP

|  (Object data - 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

Polygon Type Flag

POLYTP Object, Npolys, Default

Poly(1), Flag(1)

: :

Poly(Npolys), Flag(Npolys)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Npoly |  Number of polygons describing the geometry flag |  None  
Poly(i) |  ith polygon |   
Flag(i) |  Flag of ith polygon = 0 No flag = 1000 + n n-th Bearing surface for Extrusion ( 0 < n < 1000) |   
  
DEFINITION  
---  
POLYTP specifies the flag of the each polygon defined as geometry of an object.  
  
REMARKS  
---  
See also DIEGEO  
  
RELATED TOPICS  
---  
[DIEGEO (2D)](/docs/en/keyword_documentation/d/diegeo/), [DIEGEO (3D)](/docs/en/keyword_documentation/d/diegeo_3d/)
