---
lang: sk
title: "ELMCON (2D)"
---

# ELMCON

|  (Object data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ELMCON Object, NElem

Element(1), Nd1(1), Nd2(1), Nd3(1), Nd4(1)

: : : : :

Element(NElem), Nd1(NElem), Nd2(NElem), Nd3(NElem), Nd4(NElem)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
NElem |  Number of elements in object |  None  
Element(i) |  Element number of ith data set |  None  
Nd1(i) |  First node in element connectivity of ith data set |  None  
Nd2(i) |  Second node in element connectivity of ith data set |  None  
Nd3(i) |  Third node in element connectivity of ith data set |  None  
Nd4(i) |  Fourth node in element connectivity of ith data set |  None  
  
DEFINITION  
---  
ELMCON specifies the element connectivity of each element in an object.  
  
REMARKS  
---  
The connectivity should represent a four-noded linear element. The connectivity should be specified in a counterclockwise direction. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Object Elemental data](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/), [Mesh](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/) Keywords: [RZ (2D)](/docs/sk/keyword_documentation/r/rz/), [RZ (3D)](/docs/sk/keyword_documentation/r/rz_3d/)
