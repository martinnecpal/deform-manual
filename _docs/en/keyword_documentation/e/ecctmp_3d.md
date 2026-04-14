---
lang: en
title: "ECCTMP (3D)"
---

# ECCTMP

|  (Object data – 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

ECCTMP Object, Ndata, DefBCHeat

Num(1), node1(1) node2(1) node3(1) node4(1) BCHeat(1)

: :

Num(Ndata), node1(Ndata) node2(Ndata) node3(Ndata) node4(Ndata) BCHeat(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of face constraint data sets |  None  
DefBCHeat |  Default heat transfer boundary constraint code of all faces not listed in face constraint data pairs |  None  
Num(i) |  ith data pair |  None  
node1(i) |  1st node defining face i |   
node2(i) |  2nd node defining face i |   
node3(i) |  3rd node defining face i |   
node4(i) |  4th node defining face i |   
BCHeat(i) |  Heat transfer boundary constraint code of ith data pair |  None  
  
DEFINITION  
---  
ECCTMP specifies the heat transfer boundary constraint code for individual faces.  
  
REMARKS  
---  
The boundary constraint code (bcc) options for DefBCHeat and BCHeat(i) are 2: Heat exchanging with the environment via convection and radiation 3: heat flux 4: local definition For bcc = 2, convection and radiation heat transfer calculations will be performed at the specified face. For bcc = 3, the value of the nodal heat flux should be specified with ECHFLX or ECTMFN. For bcc = 4, the value of the nodal heat flux should be specified with LOCTMP or in a user routine. The user specifies a heat flux, an emmisivity, a convection coefficient and an environmental temperature in this boundary condition. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: ,[ECTMFN (2D)](/docs/en/keyword_documentation/e/ectmfn/), [ECTMFN (3D)](/docs/en/keyword_documentation/e/ectmfn_3d/), [BCCDFN (2D)](/docs/en/keyword_documentation/b/bccdfn/), [BCCDFN (3D)](/docs/en/keyword_documentation/b/bccdfn_3d/), [LOCTMP](/docs/en/keyword_documentation/l/loctmp/), [NDTMP (2D)](/docs/en/keyword_documentation/n/ndtmp/), [NDTMP (3D)](/docs/en/keyword_documentation/n/ndtmp_3d/), [ECHFLX (2D)](/docs/en/keyword_documentation/e/echflx/), [ECHFLX (3D)](/docs/en/keyword_documentation/e/echflx_3d/).
