---
lang: sk
title: "MSHSEC (2D3D)"
---

# MSHSEC

|  (Action keyword)  
---|---  
_Update History:_ v10.0 – MSHSEC was introduced. |  Last updated on : 24-07-2013  
  
* * *

MSHSEC Object, NumMesh

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxObject |  Number of objects to be converted |  None  
NumMesh |  Number of mesh sections |  0  
  
DEFINITION  
---  
MSHSEC specifies the number of mesh sections for 3D model conversion.  
  
REMARKS  
---  
This is action keyword usually written in DEF_MULTI.INI which is input file to M23.EXE binary which converts 2D model to 3D. If Mesh output is unselected in DEF_GUI_CNV.EXE, NumMesh is set to 0.  
  
RELATED TOPICS  
---  
[2D to 3D model conversion](/docs/sk/pre_processor/22_convert_2d_to_3d/22_convert_2d_to_3d/), M23.EXE Keywords: [GEO23](/docs/sk/keyword_documentation/g/geo23/), [GEOSEC](/docs/sk/keyword_documentation/g/geosec/), [ACTOUT](/docs/sk/keyword_documentation/a/actout/), [CRDSYS](/docs/sk/keyword_documentation/c/crdsys/), [CNVT3D](/docs/sk/keyword_documentation/c/cnvt3d/)
