---
lang: sk
title: "ECTMFN (2D)"
---

# ECTMFN

|  (Object Data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECTMFN Object, Ndata, Default

Num(1), node1(1) node2(1) BCfuncNum(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) BCfuncNum(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of edge constraint data sets |  None  
Default |  Default value for temperature function |  0  
Num(i) |  ith data set |  None  
node1(i) |  1st node defining edge i |  None  
node2(i) |  2nd node defining edge i |  None  
BCfuncNum(i) |  Function type for deformation boundary constraint in ith data set |  None  
  
DEFINITION  
---  
ECTMFN specifies whether a temperature edge boundary condition function is defined as a function or through a user subroutine.  
  
REMARKS  
---  
The function type (Ftype) options are: < 0 user routine number > 0 function number (specified in BCCFNC) The user should be aware that the edge definition function shares the function structure with the nodal boundary condition function keyword (BCCFNC). Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object Edge data: Thermal, [Boundary Constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/): Thermal-Temperature Keywords: [ECCTMP (2D)](/docs/sk/keyword_documentation/e/ecctmp/), [ECCTMP (3D)](/docs/sk/keyword_documentation/e/ecctmp_3d/), [ECTMFN (2D)](), [ECTMFN (3D)](/docs/sk/keyword_documentation/e/ectmfn_3d/), [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/), [LOCTMP](/docs/sk/keyword_documentation/l/loctmp/)
