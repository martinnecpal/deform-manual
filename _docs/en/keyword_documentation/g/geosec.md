---
lang: en
title: "GEOSEC (2D3D)"
---

# GEOSEC

|  (Action keyword)  
---|---  
_Update History:_ (New) Definition has been introduced in v10.0 |  Last updated on : 24-07-2013  
  
* * *

GEOSEC Object, NumGeo

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Number of objects to be converted |  None  
NumGeo |  Number of geometry sections |  0  
  
DEFINITION  
---  
GEOSEC specifies the number of geometry sections for 3D model conversion.  
  
REMARKS  
---  
This is action keyword usually written in DEF_MULTI.INI which is input file to M23.EXE binary which converts 2D model to 3D. If Geometry output is unselected in DEF_GUI_CNV.EXE, NumGeo is set to 0.  
  
RELATED TOPICS  
---  
[2D to 3D model conversion](/docs/en/pre_processor/22_convert_2d_to_3d/22_convert_2d_to_3d/), M23.EXE Keywords: [GEO23](/docs/en/keyword_documentation/g/geo23/), [MSHSEC](/docs/en/keyword_documentation/m/mshsec/), [ACTOUT](/docs/en/keyword_documentation/a/actout/), [CRDSYS](/docs/en/keyword_documentation/c/crdsys/), [CNVT3D](/docs/en/keyword_documentation/c/cnvt3d/)
