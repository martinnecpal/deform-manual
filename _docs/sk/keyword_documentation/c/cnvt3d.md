---
lang: sk
title: "CNVT3D (2D3D)"
---

# CNVT3D

|  (Action keyword)  
---|---  
_Update History:_ (New) Definition has been introduced in v10.0 |  Last updated on : 23-07-2013  
  
* * *

CNVT3D MaxObject

Object(1),…,Object(MaxObject)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxObject |  Number of objects to be converted |  None  
ObjectList |  ith object number |  None  
  
DEFINITION  
---  
CNVT3D specifies the 2D object list for 3D model conversion.  
  
REMARKS  
---  
This is action keyword usually written in DEF_MULTI.INI which is input file to M23.EXE binary which converts 2D model to 3D.  
  
RELATED TOPICS  
---  
[2D to 3D model conversion]({{ '/docs/sk/pre_processor/22_convert_2d_to_3d/22_convert_2d_to_3d/' | relative_url }}), M23.EXE Keywords: [GEO23]({{ '/docs/sk/keyword_documentation/g/geo23/' | relative_url }}), [GEOSEC]({{ '/docs/sk/keyword_documentation/g/geosec/' | relative_url }}), [MSHSEC]({{ '/docs/sk/keyword_documentation/m/mshsec/' | relative_url }}), [ACTOUT]({{ '/docs/sk/keyword_documentation/a/actout/' | relative_url }}), [CRDSYS]({{ '/docs/sk/keyword_documentation/c/crdsys/' | relative_url }})
