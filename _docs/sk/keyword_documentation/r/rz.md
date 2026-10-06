---
lang: sk
title: "RZ (2D)"
---

# RZ

|  (Object data - 2D)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

RZ Object, Node, X, Y

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Node  |  Node number |  None  
X |  X coordinate |  None  
Y |  Y coordinate |  None  
  
DEFINITION  
---  
RZ specifies the X and Y coordinates of each node.  
  
REMARKS  
---  
Node numbers should begin with 1 and proceed continuously to the last node. To ensure the most efficient processing of the simulation, the mesh should be optimized for profile. If this has not been done in the mesh generator, it can be done in DEFORM using keywords [DEFBWD]({{ '/docs/sk/keyword_documentation/d/defbwd/' | relative_url }}) and [TMPBWD]({{ '/docs/sk/keyword_documentation/t/tmpbwd/' | relative_url }}). Applicable object types: [Rigid]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Object Nodal Data]({{ '/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/' | relative_url }}) Keywords: [DEFBWD]({{ '/docs/sk/keyword_documentation/d/defbwd/' | relative_url }}), [TMPBWD]({{ '/docs/sk/keyword_documentation/t/tmpbwd/' | relative_url }})
