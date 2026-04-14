---
lang: en
title: "STNPAT (2D3D)"
---

# STNPAT

|  (Object data)  
---|---  
_Update History:_ V11.1 - STNPAT has been introduced. |  Last updated on : 21-05-2016  
  
* * *

STNPAT, OBJ#, NData, NType, FieldWidth, Default Value

Element(1), STNPAT(1,1) … STNPAT(1, FieldWidth)

: : :

Element(NData), STNPAT(NData,1) … STNPAT(NData, FieldWidth)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
NData |  Number of elements |  None  
nType |  Data type (0 for element data) |  0  
NDefault |  Default value |  0  
FieldWidth |  Number of partitioned strains at each element |  None  
Element(i) |  Element number for ith data set |  None  
STNPAT(i, j) |  jth STNPAT value for ith element |  None  
  
DEFINITION  
---  
Keyword STNPAT provides storage space for partitioned effective strains of child phases of each object element. The field width of the STNPAT is the number of child phases of the parent material assigned to the object.  
  
RELATED TOPICS  
---  
Keyword: TXTURE, STNOUT
