---
lang: en
title: "ELMCON (3D)"
---

# ELMCON

|  (Object data –3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

ELMCON Object, Nelem,Nnode

Element(1), Node(1,1), Node(1,2), ....., Node(1,Nnode)

: : : :

Element(Nelem), Node(Nelem,Nnode), Node(Nelem,Nnode), ....., Node(Nelem,Nnode)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Nelem |  Number of elements in object |  None  
Nnode |  Number of nodes in each element |  None  
Element(i) |  Element number of ith data set |  None  
Node(i,1) |  First node in element connectivity of ith data set |  None  
Node(i,2) |  Second node in element connectivity of ith data set |  None  
Node(i,3) |  Third node in element connectivity of ith data set |  None  
Node(i,Nnode) |  Last node in element connectivity of ith data set |  None  
  
DEFINITION  
---  
ELMCON specifies the element connectivity of each element in an object.  
  
REMARKS  
---  
The connectivity should represent either 8 noded brick elements or 4 noded tetrahedral elements as shown below with Nnode representing the number of nodes pre element. The connectivity should be specified in a counterclockwise direction. Applicable object types:[Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Object Elemental data](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/), [Mesh](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/) Keywords: [RZ (2D)](/docs/en/keyword_documentation/r/rz/), [RZ (3D)](/docs/en/keyword_documentation/r/rz_3d/)
