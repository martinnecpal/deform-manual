---
lang: sk
title: "GEO23 (2D3D)"
---

# GEO23

|  (Action keyword)  
---|---  
_Update History:_ v10.0 – GEO23 was introduced. |  Last updated on : 24-07-2013  
  
* * *

GEO23 Object, ConvType, RevType

RevAngle, StartAngle, Tolerance (for ConvType=0)

or

ExtrudeLength, StartLocation (for ConvType=1)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
ConvType |  Conversion type **0** = Revolve **1** = Extrude |  0  
RevType |  Revolve type **0** = Revolve solid **1** = Revolve hollow |  0  
RevAngle |  Revolve angle |  360  
StartAngle |  Start angle for revolve |  0  
Tolerance |  Tolerance for axisymmetry node |  0.001  
ExtrudeLength |  Extrude length |  5  
StartLocation |  Start location of extrude |  0  
  
DEFINITION  
---  
GEO23 specifies conversion type (Revolve or Extrude) and associated conversion parameters, required for 2D to 3D model conversion.  
  
REMARKS  
---  
This is action keyword usually written in DEF_MULTI.INI which is input file to M23.EXE binary. “Revolve” is default for 2D plane strain and plane stress model. “Extrude” is default for 2D axisymmetry and torsion models.  
  
RELATED TOPICS  
---  
[2D to 3D model conversion](/docs/sk/pre_processor/22_convert_2d_to_3d/22_convert_2d_to_3d/), M23.EXE Keywords: [ACTOUT](/docs/sk/keyword_documentation/a/actout/), [GEOSEC](/docs/sk/keyword_documentation/g/geosec/), [MSHSEC](/docs/sk/keyword_documentation/m/mshsec/), [CRDSYS](/docs/sk/keyword_documentation/c/crdsys/), [CNVT3D](/docs/sk/keyword_documentation/c/cnvt3d/)
