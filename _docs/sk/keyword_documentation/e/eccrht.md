---
lang: sk
title: "ECCRHT (2D)"
---

# ECCRHT

|  (Object data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECCRHT Object, Ndata, DefBCRstHt

Num(1), node1(1) node2(1) BCRstHt(1)

: :

Num(Ndata), node1(Ndata) node2(Ndata) BCRstHt(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/boundary constraint data pairs |  None  
DefBCRstHt |  Default resistance heating boundary condition code of all edges not listed. |  0  
Num(i) |  ith data pair |  None  
node1(i) |  1st node defining edge i |   
node2(i) |  2nd node defining edge i |   
BCRstHt(i) |  Resistance heating boundary constraint code of ith data pair |   
  
DEFINITION  
---  
ECCRHT specifies the resistance heating boundary condition code for individual edges.  
  
REMARKS  
---  
The boundary condition code (bcc) options for DefBCRstHt and BCRstHt(i) are: 3 = Electric current flux 4 = Local definition (not implemented) For bcc = 3, the value of the electric current flux should be specified with ECRFLX. Applicable object types: [Elastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }}), [Inter-object contact]({{ '/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/' | relative_url }}) Keywords: [ECRHFN (2D)]({{ '/docs/sk/keyword_documentation/e/ecrhfn/' | relative_url }}), [ECRHFN (3D)]({{ '/docs/sk/keyword_documentation/e/ecrhfn_3d/' | relative_url }}), [BCCFNC (2D3D)]({{ '/docs/sk/keyword_documentation/b/bccfnc/' | relative_url }}), [VOTAGE (2D3D)]({{ '/docs/sk/keyword_documentation/v/votage/' | relative_url }}), [ECRFLX (2D)]({{ '/docs/sk/keyword_documentation/e/ecrflx/' | relative_url }}), [ECRFLX (3D)]({{ '/docs/sk/keyword_documentation/e/ecrflx_3d/' | relative_url }})
