---
lang: sk
title: "ECCDEF (3D)"
---

# ECCDEF

|  (Object data – 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

ECCDEF Object, Ndata, Default

Num(1), Node1(1), Node2(1) node3(1) node4(1) NCode(1)

: : :

Num(Ndata), Node1(Ndata), Node2(Ndata) node3(Ndata) node4(Ndata) NCode(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of face constraint data sets |  None  
Default |  Default boundary constraint |  None  
Num(i) |  Node of ith data set None |   
node1(i) |  1st node defining face i |   
node2(i) |  2nd node defining face i |   
node3(i) |  3rd node defining face i |   
node4(i) |  4th node defining face i |   
NCode(i) |  Deformation boundary constraint code of ith data set |  None  
  
DEFINITION  
---  
ECCDEF specifies the deformation boundary constraint on a specified face.  
  
REMARKS  
---  
The face boundary constraint code (bcc) options are 2: face pressure 9: local definition For ecc = 2, the value of the nodal traction should be specified with keyword ECPRES. Only normal pressure can only be applied to faces. The keyword ECDEFN is used to specify if the face values are specified as a constant, a function of time or by a user routine (Note: The user routine option is not available in the NT versions of 2D). For ecc = 9, the local boundary conditions are specified with LOCDEF. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
|  [Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)  
---  
  
Keywords: [ECDEFN (2D)](/docs/sk/keyword_documentation/e/ecdefn/), [ECDEFN (3D)](/docs/sk/keyword_documentation/e/ecdefn_3d/), [ECPRES (2D)](/docs/sk/keyword_documentation/e/ecpres/), [ECPRES (3D)](/docs/sk/keyword_documentation/e/ecpres_3d/), [LOCDEF (2D)](/docs/sk/keyword_documentation/l/locdef/), [LOCDEF (3D)](/docs/sk/keyword_documentation/l/locdef_3d/)
