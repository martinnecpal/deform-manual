---
lang: sk
title: "DRZ (2D)"
---

# DRZ

|  (Material Data - 2D)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

DRZ Object, Ndata, DefXDisp, DefYDisp

Node(1), XDisp(1), YDisp(1)

: : :

Node(Ndata), XDisp(Ndata), YDisp(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/displacement sets |  None  
DefXDisp |  Default nodal displacement in X of all nodes not listed in the node/displacement sets |  0  
DefYDisp |  Default nodal displacement in Y of all nodes not listed in the node/displacement sets |  0  
Node(i) |  Node number of ith data set |  None  
XDisp(i) |  Displacement in X of ith data set |  0  
YDisp(i) |  Displacement in Y of ith data set |  0  
  
DEFINITION  
---  
DRZ is a boundary constraint used to apply a shrink fit to an object boundary.  
  
REMARKS  
---  
XDisp(i) or YDisp(i) should specify the amount of shrink fit interference. The interference can be applied in the global X or Y direction. The sign of the interference value (positive or negative) should indicate the direction of displacement occurring between the pre-assembly and post-assembly geometry of the constrained object. The shrink fit constraint should be assigned to the interface contact nodes of either of the contacting objects, but should not be assigned to both. Shrink fit constraints can only be applied to elastic objects. If no value is specified for DefXDisp and/or DefYDisp, they will be assumed to be zero.  
  
RELATED TOPICS  
---  
[Object Advanced nodal data](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/) Keyword: [RZ(2D)](/docs/sk/keyword_documentation/r/rz/)
