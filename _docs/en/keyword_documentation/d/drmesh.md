---
lang: en
title: "DRMESH (3D)"
---

# DRMESH

|  (Object data –3D)  
---|---  
_Update History:_ (New definition has been introduced in v10.0) |  Last updated on : 13-08-2013  
  
* * *

DRMESH Object, Ndata, DefXDisp, DefYDisp, DefZDisp

Node(1), XDisp(1), YDisp(1 ,ZDisp(1)

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
DRMESH is the nodal displacement since the creation of current mesh.  
  
REMARKS  
---  
This state variable is used to determine the quality of current mesh. It is initialized to zero for a new mesh. The format of this keyword is very similar to DRZ.  
  
RELATED TOPICS  
---  
[Object Advanced nodal data](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) Keyword: [DRZ(2D)](/docs/en/keyword_documentation/d/drz/), [DRZ (3D)](/docs/en/keyword_documentation/d/drz_3d/)
