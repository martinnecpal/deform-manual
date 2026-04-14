---
lang: en
title: "RHTFLX (2D3D)"
---

# RHTFLX

|  (Object Data)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

RHTFLX Object, Ndata, DefFlux

Node(1), Flux(1)

: :

Node(Ndata), Flux(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/flux pairs |  None  
DefFlux |  Default distributed nodal current flux of all nodes not listed in the node/flux pairs with resistance heating boundary constraint code 3. |  0.0  
Node(i) |  Node number of ith data pair |  None  
Flux(i) |  Distributed nodal current flux of ith data pair |  0.0  
  
DEFINITION  
---  
RHTFLX specifies current flux for the surface of work.  
  
REMARKS  
---  
Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [DATOM](/docs/en/keyword_documentation/d/datom/), [BCCCRB (2D)](/docs/en/keyword_documentation/b/bcccrb/), [BCCCRB (3D)](/docs/en/keyword_documentation/b/bcccrb_3d/)
