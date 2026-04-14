---
lang: en
title: "CUSVAR (2D3D)"
---

# CUSVAR

|  (Object data)  
---|---  
_Update History:_ (New keyword in v11) |  Last updated on : 23-07-2013  
  
* * *

CUSVAR Object, VarNo, VarDefType, Ndata, Default, Ncomp

Num(1), Data(1,1),...,Data(1, Ncomp)

:: :: ::

Num(Ndata), Data(Ndata,1),...,Data(Ndata, Ncomp)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
VarNo |  Variable number |  None  
VarDefType |  = **0** defined on any = ******1** defined on nodes = **2** defined on elements |  0  
Ndata |  Number of custom variables |  None  
Default |  Default value |  0  
Ncomp |  Number of components |  0  
Num(i) |  Number of ith custom variable |  0  
Data(i,j) |  Value of of jth component at ith variable |  0  
  
DEFINITION  
---  
CUSVAR stores the values of custom state variables which are usually imported from 3rd party software.  
  
REMARKS  
---  
This keyword is used together with CVNAME which stores custom variable’s name and its component’s name.  
  
RELATED TOPICS  
---  
Related keywords: [CVNAME](/docs/en/keyword_documentation/c/cvname/), [USRNOD](/docs/en/keyword_documentation/u/usrnod/), [USRELM](/docs/en/keyword_documentation/u/usrelm/), [UNNAME](/docs/en/keyword_documentation/u/unname/)
