---
lang: sk
title: "NDHEAT (2D3D)"
---

# NDHEAT

|  (Object data)  
---|---  
|  Last updated on : 12-08-2014  
  
* * *

NDHEAT Object, Ndata, DefHeat

Node(1), Heat(1)

: :

Node(Ndata), Heat(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/heat pairs |  None  
DefHeat |  Default nodal heat of all nodes not listed in the node/heat pairs with heat transfer boundary constraint code 0. |  0.0  
Node(i) |  Node number of ith data pair |  None  
Heat(i) |  Nodal heat of ith data pair |  0.0  
  
DEFINITION  
---  
NDHEAT specifies the nodal heat to be applied to individual nodes.  
  
REMARKS  
---  
If no value is specified for DefHeat, it is assumed to be zero. Nodal heat values may not be applied to nodes which have heat transfer boundary constraint code 0 ([BCCTMP]({{ '/docs/sk/keyword_documentation/b/bcctmp/' | relative_url }})). Nodal heat may be specified as a function of time with keyword [BCCFNC]({{ '/docs/sk/keyword_documentation/b/bccfnc/' | relative_url }}). Applicable object types: : [Rigid]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Object Nodal Data]({{ '/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/' | relative_url }}):Thermal Keyword: [BCCTMP]({{ '/docs/sk/keyword_documentation/b/bcctmp/' | relative_url }}), [BCCFNC]({{ '/docs/sk/keyword_documentation/b/bccfnc/' | relative_url }})
