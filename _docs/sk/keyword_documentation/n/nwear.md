---
lang: sk
title: "NWEAR (2D3D)"
---

# NWEAR

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

NWEAR ObjNo, NumNd, DefaultVal

Node(1), IntTemp(1), SldVel(1), IntPrs(1), InsWrDpth(1), TotalWrDepth(1)

Node(NumNd), IntTemp(NumNd), SldVel(NumNd), IntPrs(NumNd), InsWrDpth(NumNd), TotalWrDepth(NumNd)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
ObjNo |  Object Number |  None  
NumNd |  Number of nodes |  None  
Node(1) |  Node number |   
IntTemp(1) |  Interface temperature |   
SldVel(1)  |  Sliding velocity |   
IntPrs(1) |  Interface pressure |   
InsWrDpth(1) |  Instant wear depth |   
TotalWrDepth(1) |  Total wear depth |   
  
DEFINITION  
---  
NWEAR specifies wear data at a node.  
  
REMARKS  
---  
Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic).  
  
RELATED TOPICS  
---  
[Object Nodal Data](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/) Keywords: [WMODEL](/docs/sk/keyword_documentation/w/wmodel/)
