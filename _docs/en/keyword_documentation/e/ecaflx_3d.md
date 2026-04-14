---
lang: en
title: "ECAFLX (3D)"
---

# ECAFLX

|  (Object data – 3D)  
---|---  
_Update History:_ (New definition has been introduced in v10.0) |  Last updated on : 13-08-2013  
  
* * *

ECAFLX Object1, Ndata, Default

Num(1), node1(1) node2(1) node3(1) node4(1) Flux(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) node3(Ndata) node4(Ndata) Flux(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of face data sets |  None  
Default |  Default value for edge based atom flux |  0.0  
Num(i) |  ith data pair |  None  
node1(i) |  1st node defining face i |   
node2(i) |  2nd node defining face i |   
node3(i) |  3rd node defining face i |   
node4(i) |  4th node defining face i |   
Flux(i) |  Distributed atom flux of ith data pair |  0.0  
  
DEFINITION  
---  
ECAFLX specifies the distributed atom heat flux to be applied to individual faces.  
  
REMARKS  
---  
Distributed atom flux is defined as atom per unit time per unit area. The atom flux is assumed to be constant over the edge it is defined over. In order to activate atom flux, the faces must be specified using the keyword ECCATM with a boundary condition code of 3. Atom flux may be specified as a function of time with keyword ECATFN. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object data: [Diffusion](/docs/en/pre_processor/10_material_data/10_4_diffusion_data/10_4_diffusion_data/) Keywords: [ECCATM(2D),](/docs/en/keyword_documentation/e/eccatm/) [ECCATM (3D)](/docs/en/keyword_documentation/e/eccatm_3d/), [ECTMFN (2D)](/docs/en/keyword_documentation/e/ectmfn/), [ECTMFN (3D)](/docs/en/keyword_documentation/e/ectmfn_3d/)
