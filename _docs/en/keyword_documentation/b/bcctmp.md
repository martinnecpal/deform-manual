---
lang: en
title: "BCCTMP (2D3D)"
---

# BCCTMP

|  (Object Data)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

BCCTMP Object, Ndata, DefBCHeat  
Node(1), BCHeat(1)  
: :  
Node(Ndata), BCHeat(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/boundary constraint data pairs |  None  
DefBCHeat |  Default heat transfer boundary constraint code of all nodes not listed in node/boundary constraint data pairs |  None  
Node(i) |  Node number of ith data pair |  None  
BCHeat(i) |  Heat transfer boundary constraint code of ith data Pair |  None  
  
DEFINITION  
---  
BCCTMP specifies the heat transfer boundary constraint code for individual nodes.  
  
REMARKS  
---  
The boundary constraint code (bcc) options for DefBCHeat and BCHeat(i) are: 0 nodal heat 1 nodal temperature 2 node is exchanging heat with the environment via convection and radiation  3 nodal heat flux  -n node is in contact with object n For bcc = 0, the value of the nodal heat should be specified with NDHEAT or BCCFNC. For bcc = 1, the value of the nodal temperature should be specified with NDTMP or BCCFNC. For bcc = 2, convection and radiation heat transfer calculations will be performed at the specified node. For bcc = 3, the value of the nodal heat flux should be specified with NDFLUX or BCCFNC. For bcc = -n, conduction heat transfer calculations between object Object and object n will be performed at the specified node. For non-isothermal simulations, contact boundary constraint are updated by DEFORM during the simulation to account for nodal contact and separation associated with the object's deformation. Contact constraints are only applied to slave objects. Each node may only be assigned one type of boundary constraint code. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [BCCTFN](/docs/en/keyword_documentation/b/bcctfn/), [BCCFNC](/docs/en/keyword_documentation/b/bccfnc/), [NDHEAT](/docs/en/keyword_documentation/n/ndheat/), [NDTMP(2D)](/docs/en/keyword_documentation/n/ndtmp/), [NDTMP(3D)](/docs/en/keyword_documentation/n/ndtmp_3d/), [NDFLUX](/docs/en/keyword_documentation/n/ndflux/).
