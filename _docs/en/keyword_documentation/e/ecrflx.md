---
lang: en
title: "ECRFLX (2D)"
---

# ECRFLX

|  (Object Data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECRFLX Object1, Ndata, Default

Num(1), node1(1) node2(1) Flux(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) Flux(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of edge data sets |  None  
Default |  Default value for edge electric current flux |  0  
Num(i) |  ith data pair |   
node1(i) |  1st node defining edge i |   
node2(i) |  2nd node defining edge i |  None  
Flux(i) |  Distributed electric current flux of ith data pair |  None  
  
DEFINITION  
---  
ECRFLX specifies the distributed electric current flux to be applied to individual edges.  
  
REMARKS  
---  
Distributed electric current flux is defined as electric current per unit time per unit area. The electric current flux is assumed to be constant over the edge it is defined over. In order to activate electric current flux, the edges must be specified using the keyword ECCRHT with a boundary condition code of 3. Electric current flux may be specified as a function of time with keyword ECRHFN. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object Edge data: Electric Heating, [Boundary Constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): Heating Keywords: [ECCRHT (2D)](/docs/en/keyword_documentation/e/eccrht/), [ECCRHT (3D)](/docs/en/keyword_documentation/e/eccrht_3d/), [ECRHFN (2D)](/docs/en/keyword_documentation/e/ecrhfn/), [ECRHFN (3D)](/docs/en/keyword_documentation/e/ecrhfn_3d/)
