---
lang: en
title: "VOTAGE (2D3D)"
---

# VOTAGE

|  (Object data  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

VOTAGE Object1, Ndata, DefVtg

Node(1), Vtg(1)

: :

Node(Ndata), Vtg(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number |  None  
Ndata |  Number of node/votage pairs |  None  
DefVtg |  Default nodal votage of all nodes not listed in the node/votage pairs |  0.0  
Node(i) |  Node number of ith data pair |  None  
Vtg(i) |  Nodal votage of ith data pair |  0.0  
  
DEFINITION  
---  
VOTAGE specifies the nodal voltage to be applied to individual nodes.  
  
REMARKS  
---  
Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object Nodal Data: [Electric Heating](../../pre_processor/17_object_data_initialization/17_1_node_data_window.htm#17_1_6_Electric_Heating_Tab)
