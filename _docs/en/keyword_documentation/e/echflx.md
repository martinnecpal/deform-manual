---
lang: en
title: "ECHFLX (2D)"
---

# ECHFLX

|  (Object data -2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECHFLX Object1, Ndata, Default

Num(1), node1(1) node2(1) Flux(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) Flux(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of edge constraint data sets |  None  
Default |  Default value for heat flux |  0  
Num(i) |  ith data pair |  None  
node1(i) |  1st node defining edge i |   
node2(i) |  2nd node defining edge i |   
Flux(i) |  Distributed heat flux of ith data pair |  0  
  
DEFINITION  
---  
ECHFLX specifies the distributed heat flux to be applied to individual edges. This keyword will replace the keyword NDFLUX in versions after 2D 7.0.  
  
REMARKS  
---  
Distributed heat flux is defined as heat per unit time per unit area. The heat flux is assumed to be constant over the edge it is defined over. In order to activate heat flux, the edges must be specified using the keyword ECCTMP with a boundary condition code of 3. Nodal heat flux may be specified as a function of time with keyword ECTMFN. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object Edge data: Heat transfer, [Boundary Constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): Heat flux Keywords: [ECCTMP (2D)](/docs/en/keyword_documentation/e/ecctmp/), [ECCTMP (3D)](/docs/en/keyword_documentation/e/ecctmp_3d/), [ECTMFN (2D)](/docs/en/keyword_documentation/e/ectmfn/), [ECTMFN (3D)](/docs/en/keyword_documentation/e/ectmfn_3d/), [LOCTMP](/docs/en/keyword_documentation/l/loctmp/), [NDFLUX](/docs/en/keyword_documentation/n/ndflux/)
