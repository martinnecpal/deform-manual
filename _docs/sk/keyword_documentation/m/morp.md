---
lang: sk
title: "MORP (2D3D)"
---

# MORP

|  (Action keyword)  
---|---  
_Update History:_ V11 – MORP has been introduced. |  Last updated on : 24-07-2013  
  
* * *

MORP MorpType, NumVars

DOE_var(1)

::

DOE_var(NumVars)

SourceGeo_file

TargetGeo_file(1)

COR_file(1)

::

TargetGeo_file(NumVars)

COR_file(NumVars)

OutputGeo_file

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MorpType |  Morphing type = **1** for finding COR = **2** for morphing |  2  
NumVars |  Number of parameters for DOE variables |  None  
DOE_var(i) |  ith DOE variable number |  None  
SourceGeo_file |  Source geometry file name |  None  
TargetGeo _file(i) |  ith Target geometry file name |  None  
COR_file(i) |  ith COR file name |  None  
OutputGeo _file |  Output geometry file name |  None  
  
DEFINITION  
---  
MORP specifies the source, target, and output geometries for morphing with associated DOE variable numbers.  
  
REMARKS  
---  
This is action keyword which will create DEF_MORP2.INI and spawn DEF_MPRP2.EXE. The newly created geometry as a result of morphing will be loaded by action keyword [GFREAD](/docs/sk/keyword_documentation/g/gfread/). If nominal/source object has mesh, new mesh will be created from action keyword [DEFAMG](/docs/sk/keyword_documentation/d/defamg/). DOE variable numbers will be converted to weighting factors by parsing.  
  
RELATED TOPICS  
---  
Related keywords: [GFREAD](/docs/sk/keyword_documentation/g/gfread/), [DEFAMG](/docs/sk/keyword_documentation/d/defamg/)
