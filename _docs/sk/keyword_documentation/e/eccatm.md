---
lang: sk
title: "ECCATM (2D)"
---

# ECCATM

|  (Object Data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECCATM Object, Ndata, DefBCAtom

Num(1), node1(1) node2(1) BCAtom(1)

: :

Num(Ndata), node1(Ndata) node2(Ndata) BCAtom(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/boundary constraint data pairs |  None  
DefBCAtom |  Default carbon boundary constraint code of all edges not listed in node/boundary constraint data pairs |  0  
Num(i) |  ith data pair |   
node1(i) |  1st node defining edge i |   
node2(i) |  2nd node defining edge i |   
BCAtom(i) |  Carbon boundary constraint code of ith data Pair |  None  
  
DEFINITION  
---  
ECCATM specifies the diffusion boundary condition code for individual edges.  
  
REMARKS  
---  
The boundary constraint code (bcc) options for DefBCAtom and BCAtom(i) are: 1 edges are absorbing carbon from the environment 3 atom flux 4 local definition For bcc = 2, carbon absorption from environment calculations will be performed at the specified edge. For bcc = 3, the value of the atom flux should be specified with ECAFLX. For bcc = 4, the value of the edge atom flux should be specified with LOCATM or in a user routine. The user specifies both an atom flux and environmental atom diffusion in this boundary condition. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [ECTMFN(2D)](/docs/sk/keyword_documentation/e/ectmfn/), [ECTMFN(3D)](/docs/sk/keyword_documentation/e/ectmfn_3d/) , [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/), [LOCTMP](/docs/sk/keyword_documentation/l/loctmp/), [NDTMP(2D)](/docs/sk/keyword_documentation/n/ndtmp/), [NDTMP(3D)](/docs/sk/keyword_documentation/n/ndtmp_3d/), [ECHFLX(2D)](/docs/sk/keyword_documentation/e/ecrflx/), [ECRFLX (3D)](/docs/sk/keyword_documentation/e/ecrflx_3d/)
