---
lang: sk
title: "NDFLUX (2D3D)"
---

# NDFLUX

|  (Object data)  
---|---  
|  Last updated on : 12-08-2014  
  
* * *

NDFLUX Object1, Ndata, DefFlux

Node(1), Flux(1)

: :

Node(Ndata), Flux(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/flux pairs |  None  
DefFlux |  Default distributed nodal heat flux of all nodes not listed in the node/flux pairs with heat transfer boundary constraint code 3. |  0.0  
Node(i) |  Node number of ith data pair |  None  
Flux(i) |  Distributed nodal heat flux of ith data pair |  0.0  
  
DEFINITION  
---  
NDFLUX specifies the distributed nodal heat flux to be applied to individual nodes.  
  
REMARKS  
---  
Distributed heat flux is defined as heat per unit time per unit area. The heat flux is assumed to be linear between adjacent nodes. Using the heat flux values, resultant nodal heat is calculated for each node with a heat flux boundary constraint. The heat flux constraint will be applied to the element faces lying between the selected boundary nodes. If no value is specified for DefFlux, it is assumed to be zero. Distributed heat flux values may only be applied to nodes which have heat transfer boundary constraint code 3 ([BCCTMP](/docs/sk/keyword_documentation/b/bcctmp/)). Nodal heat flux may be specified as a function of time with keyword [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/). Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Object Nodal Data](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/):Thermal Keyword: [BCCTMP](/docs/sk/keyword_documentation/b/bcctmp/), [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/)
