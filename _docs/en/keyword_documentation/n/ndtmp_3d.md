---
lang: en
title: "NDTMP (3D)"
---

# NDTMP

|  (Object data - 3D)  
---|---  
|  Last updated on : 12-08-2014  
  
* * *

NDTMP Object1, Ndata, DefTemp

Node(1), Temp(1)

: :

Node(Ndata), Temp(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number |  None  
Ndata |  Number of node/temperature pairs |  None  
DefTemp |  Default nodal temperature of all nodes not listed in the node/temperature pairs with heat transfer boundary constraint code 1 |  0.0  
Node(i) |  Node number of ith data pair |  None  
Temp(i) |  Nodal temperature of ith data pair |  0.0  
  
DEFINITION  
---  
NDTMP specifies the nodal temperature to be applied to individual nodes.  
  
REMARKS  
---  
If no value is specified for DefTemp, it is assumed to be zero. Nodal temperature values may not be applied to nodes which have heat transfer boundary constraint code 1 ([BCCTMP]({{ '/docs/en/keyword_documentation/b/bcctmp/' | relative_url }})). Nodal temperature may be specified as a function of time with keyword [BCCFNC]({{ '/docs/en/keyword_documentation/b/bccfnc/' | relative_url }}). Applicable object types: [Rigid]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Object Nodal Data]({{ '/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/' | relative_url }}):Thermal Keyword: [BCCTMP]({{ '/docs/en/keyword_documentation/b/bcctmp/' | relative_url }}), [BCCFNC]({{ '/docs/en/keyword_documentation/b/bccfnc/' | relative_url }})
