---
lang: sk
title: "ECRFLX (3D)"
---

# ECRFLX

|  (Object data –3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

ECRFLX Object1, Ndata, Default

Num(1), node1(1) node2(1) node3(1) node4(1) Flux(1)

: : 

Num(Ndata), node1(Ndata) node2(Ndata) node3(Ndata) node4(Ndata) Flux(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of face data sets |  None  
Default |  Default value for face electric current flux |  0.0  
Num(i) |  ith data pair |  None  
node1(i) |  1st node defining face i |   
node2(i) |  2nd node defining face i |   
node3(i) |  3rd node defining face i |   
node4(i) |  4th node defining face i |   
Flux(i) |  Distributed electric current flux of ith data pair |   
  
DEFINITION  
---  
ECRFLX specifies the distributed electric current flux to be applied to individual faces.  
  
REMARKS  
---  
Distributed electric current flux is defined as electric current per unit time per unit area. The electric current flux is assumed to be constant over the face it is defined over. In order to activate electric current flux, the edges must be specified using the keyword ECCRHT with a boundary condition code of 3. Electric current flux may be specified as a function of time with keyword ECRHFN. Applicable object types: : [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object Edge data: Electric Heating, [Boundary Constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/): Heating Keywords: [ECCRHT (2D)](/docs/sk/keyword_documentation/e/eccrht/), [ECCRHT (3D)](/docs/sk/keyword_documentation/e/eccrht_3d/), [ECRHFN (2D)](/docs/sk/keyword_documentation/e/ecrhfn/), [ECRHFN (3D)](/docs/sk/keyword_documentation/e/ecrhfn_3d/)
