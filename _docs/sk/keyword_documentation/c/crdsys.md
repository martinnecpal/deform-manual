---
lang: sk
title: "CRDSYS (2D3D)"
---

# CRDSYS

|  (Action keyword)  
---|---  
_Update History:_ (New) Definition has been introduced in v10.0 |  Last updated on : 23-07-2013  
  
* * *

CRDSYS Object, AxisUp

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisUp |  Coordinate system definition =3 Z is up: X(R)->X, Y(Z)->Z =2 Y is up: X(R)->X, Y(Z)->Y |  None  
  
DEFINITION  
---  
CRDSYS specifies the 3D coordinate system setup when 2D model is converted to 3D model.  
  
REMARKS  
---  
This is action keyword usually written in DEF_MULTI.INI which is input file to M23.EXE binary which converts 2D model to 3D.  
  
RELATED TOPICS  
---  
[2D to 3D model conversion](/docs/sk/pre_processor/22_convert_2d_to_3d/22_convert_2d_to_3d/), M23.EXE Keywords: [GEO23](/docs/sk/keyword_documentation/g/geo23/), [GEOSEC](/docs/sk/keyword_documentation/g/geosec/), [MSHSEC](/docs/sk/keyword_documentation/m/mshsec/), [ACTOUT](/docs/sk/keyword_documentation/a/actout/), [CNVT3D](/docs/sk/keyword_documentation/c/cnvt3d/)
