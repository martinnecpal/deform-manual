---
lang: sk
title: "DRZ (3D)"
---

# DRZ

|  (Object Data -3D)  
---|---  
|  Last updated on : 27-09-2023  
  
* * *

DRZ Object, Ndata, DefXDisp, DefYDisp, DefZDisp

Node(1), XDisp(1), YDisp(1 , ZDisp(1)

: : : :

Node(Ndata), XDisp(Ndata), YDisp(Ndata), ZDisp(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/displacement sets |  None  
DefXDisp |  Default nodal displacement in X of all nodes not listed in the node/displacement sets |  0.0  
DefYDisp |  Default nodal displacement in Y of all nodes not listed in the node/displacement sets |  0.0  
DefZDisp |  Default nodal displacement in Z of all nodes not listed in the node/displacement sets |  0.0  
Node(i) |  Node number of ith data set |  None  
XDisp(i) |  Displacement in X of ith data set |  0.0  
YDisp(i) |  Displacement in Y of ith data set |  0.0  
ZDisp(i) |  Displacement in Z of ith data set |  0.0  
  
DEFINITION  
---  
DRZ is a boundary constraint used to apply a shrink fit to an object boundary.  
  
REMARKS  
---  
Xdisp(i), Ydisp(i), or Zdisp(i) should specify the amount of shrink fit interference. The interference can be applied in the global X, Y, or Z direction. The sign of the interference value (positive or negative) should indicate the direction of displacement occurring between the pre-assembly and post-assembly geometry of the constrained object. The shrink fit constraint should be assigned to the interface contact nodes of either of the contacting objects, but should not be assigned to both. Shrink fit constraints can only be applied to elastic objects. If no value is specified for DefXDisp DefYDisp, and/or DefZDisp they will be assumed to be zero.  
  
RELATED TOPICS  
---  
[Object Advanced nodal data](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/) Keyword: [RZ(3D)](/docs/sk/keyword_documentation/r/rz_3d/)
