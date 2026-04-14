---
lang: sk
title: "ECCRHT (3D)"
---

# ECCRHT

|  (Object data – 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

ECCRHT Object, Ndata, DefBCRstHt

Num(1), node1(1) node2(1) node3(1) node4(1) BCRstHt(1)

: :

Num(Ndata), node1(Ndata) node2(Ndata) node3(Ndata) node4(Ndata) BCRstHt(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of face constraint data sets |  None  
DefBCRstHt |  Default resistance heating boundary condition code of all faces not listed in face constraint data pairs |   
Num(i) |  ith data pair |  None  
node1(i) |  1st node defining face i |   
node2(i) |  2nd node defining face i |   
node3(i) |  3rd node defining face i |   
node4(i) |  4th node defining face i |   
BCRstHt(i) |  Resistance heating boundary constraint code of ith data pair |   
  
DEFINITION  
---  
ECCRHT specifies the resistance heating boundary condition code for individual faces.  
  
REMARKS  
---  
The boundary condition code (bcc) options for DefBCRstHt and BCRstHt(i) are 3 = Electric current flux 4 = local definition (not implemented) For bcc = 3, the value of the electric current flux should be specified with ECRFLX. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [ECRHFN (2D)](/docs/sk/keyword_documentation/e/ecrhfn/), [ECRHFN (3D)](/docs/sk/keyword_documentation/e/ecrhfn_3d/), [BCCFNC (2D3D)](/docs/sk/keyword_documentation/b/bccfnc/), [VOTAGE (2D3D)](/docs/sk/keyword_documentation/v/votage/), [ECRFLX (2D)](/docs/sk/keyword_documentation/e/ecrflx/), [ECRFLX (3D)](/docs/sk/keyword_documentation/e/ecrflx_3d/)
