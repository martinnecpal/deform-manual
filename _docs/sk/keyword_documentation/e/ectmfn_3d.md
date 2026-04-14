---
lang: sk
title: "ECTMFN (3D)"
---

# ECTMFN

|  (Object data – 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

ECTMFN Object, Ndata, Default

Num(1), node1(1) node2(1) node3(1) node4(1) BCfuncNum(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) node3(Ndata) node4(Ndata) BCfuncNum(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of face constraint data sets |  None  
Default |  Default value for temperature function |  0  
Num(i) |  ith data set |  None  
node1(i) |  1st node defining face i |  None  
node2(i) |  2nd node defining face i |  None  
node3(i) |  3rd node defining face i |   
node4(i) |  4th node defining face i |   
BCfuncNum(i) |  Function type for deformation boundary constraint in ith data set |  None  
  
DEFINITION  
---  
ECTMFN specifies whether a temperature face boundary condition function is defined as a function or through a user subroutine.  
  
REMARKS  
---  
The function type (Ftype) options are: < 0 user routine number > 0 function number (specified in BCCFNC) The user should be aware that the face definition function shares the function structure with the nodal boundary condition function keyword (BCCFNC). Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object Edge data: Thermal, [Boundary Constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/): Thermal-Temperature Keywords: [ECCTMP (2D)](/docs/sk/keyword_documentation/e/ecctmp/), [ECCTMP (3D)](/docs/sk/keyword_documentation/e/ecctmp_3d/), [ECTMFN (2D)](/docs/sk/keyword_documentation/e/ectmfn/), [ECTMFN (3D)](), [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/), [LOCTMP](/docs/sk/keyword_documentation/l/loctmp/)
