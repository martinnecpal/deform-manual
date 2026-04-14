---
lang: sk
title: "CVNAME (2D3D)"
---

# CVNAME

|  (Simulation control)  
---|---  
_Update History:_ (New keyword in v11) |  Last updated on : 23-07-2013  
  
* * *

CVNAME VarNo, Ncomp

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
VarNo |  Custom variable number |  0  
Ncomp |  Number of components |  0  
VarName |  Custom variable name |  None  
CompName(i) |  Name of ith component |  None  
  
DEFINITION  
---  
CVNAME stores the name of custom variable and its component’s names.  
  
REMARKS  
---  
This keyword can be used to import custom state variable from 3rd party software. It is used together with CUSVAR which stores the values of custom variables.  
  
RELATED TOPICS  
---  
Keyword: [CUSVAR](/docs/sk/keyword_documentation/c/cusvar/), [USRNOD](/docs/sk/keyword_documentation/u/usrnod/), [USRELM](/docs/sk/keyword_documentation/u/usrelm/), [UNNAME](/docs/sk/keyword_documentation/u/unname/)
