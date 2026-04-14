---
lang: en
title: "DEFFRZ (2D3D)"
---

# DEFFRZ

|  (Action keyword)  
---|---  
_Update History:_ (V11.1 - DEFFRZ has been introduced.) |  Last updated on : 21-05-2016  
  
* * *

DEFINT Object, Workpiece, Tol

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Workpiece |  Workpiece number |  None  
Tol |  Interpolation tolerance |  0.0  
  
DEFINITION  
---  
DEFFRZ specifies the force interpolation, which will generate force BCC for Die Stress Analysis.  
  
REMARKS  
---  
In Die Stress Analysis, we need to get the die force BBC, interpolated from workpiece force. In general, the tolerance can be 0.0 or user specified value. We use this keyword for Die Stress Analysis in batch mode.  
  
RELATED TOPICS  
---  
Related keywords: [DEFINT](/docs/en/keyword_documentation/d/defint/)
