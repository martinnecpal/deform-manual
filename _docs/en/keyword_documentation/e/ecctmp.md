---
lang: en
title: "ECCTMP (2D)"
---

# ECCTMP

|  (Object Data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECCTMP Object, Ndata, DefBCHeat

Num(1), node1(1) node2(1) BCHeat(1)

: :

Num(Ndata), node1(Ndata) node2(Ndata) BCHeat(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of edge constraint data sets |  None  
DefBCRstHt |  Default heat transfer boundary constraint code of all edges not listed in edge constraint data pairs |  None  
Num(i) |  ith data pair |   
node1(i) |  1st node defining edge i |   
node2(i) |  2nd node defining edge i |   
BCRstHt(i) |  Heat transfer boundary constraint code of ith data |  None  
  
DEFINITION  
---  
ECCTMP specifies the heat transfer boundary constraint code for individual edges.  
  
REMARKS  
---  
The boundary constraint code (bcc) options for DefBCHeat and BCHeat(i) are: 1 node is exchanging heat with the environment via convection and radiation 3 heat flux 4 local definition For bcc = 2, convection and radiation heat transfer calculations will be performed at the specified edge. For bcc = 3, the value of the nodal heat flux should be specified with ECHFLX or ECTMFN. For bcc = 4, the value of the nodal heat flux should be specified with LOCTMP or in a user routine. The user specifies a heat flux, an emmisivity, a convection coefficient and an environmental temperature in this boundary condition. Applicable object types: [Elastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints]({{ '/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }}), [Inter-object contact]({{ '/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/' | relative_url }}) Keywords: ,[ECTMFN (2D)]({{ '/docs/en/keyword_documentation/e/ectmfn/' | relative_url }}), [ECTMFN (3D)]({{ '/docs/en/keyword_documentation/e/ectmfn_3d/' | relative_url }}), [BCCDFN (2D)]({{ '/docs/en/keyword_documentation/b/bccdfn/' | relative_url }}), [BCCDFN (3D)]({{ '/docs/en/keyword_documentation/b/bccdfn_3d/' | relative_url }}), [LOCTMP]({{ '/docs/en/keyword_documentation/l/loctmp/' | relative_url }}), [NDTMP (2D)]({{ '/docs/en/keyword_documentation/n/ndtmp/' | relative_url }}), [NDTMP (3D)]({{ '/docs/en/keyword_documentation/n/ndtmp_3d/' | relative_url }}), [ECHFLX (2D)]({{ '/docs/en/keyword_documentation/e/echflx/' | relative_url }}), [ECHFLX (3D)]({{ '/docs/en/keyword_documentation/e/echflx_3d/' | relative_url }}).
