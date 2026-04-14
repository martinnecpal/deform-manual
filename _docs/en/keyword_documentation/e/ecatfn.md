---
lang: en
title: "ECATFN (2D)"
---

# ECATFN

|  (Object data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECATFN Object, Ndata, Default

Num(1), node1(1) node2(1) BCfuncNum(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) BCfuncNum(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of edge constraint data sets |  None  
Default |  Default value for function number |  0  
Num(i) |  ith data set |  None  
node1(i) |  1st node defining edge i |  None  
node2(i) |  2nd node defining edge i |  None  
BCfuncNum(i) |  Function type for diffusion boundary constraint in ith data Set |  None  
  
DEFINITION  
---  
ECATFN specifies whether a atom edge boundary condition function is defined as a function or through a user subroutine.  
  
REMARKS  
---  
The function type (Ftype) options are: < 0 user routine number > 0 function number (specified in [BCCFNC](/docs/en/keyword_documentation/b/bccfnc/)) The user should be aware that the edge definition function shares the function structure with the nodal boundary condition function keyword ([BCCFNC](/docs/en/keyword_documentation/b/bccfnc/)). Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object Edge data: Diffusion, [Boundary Constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) Keywords: [BCCFNC](/docs/en/keyword_documentation/b/bccfnc/), [ECCATM(2D)](/docs/en/keyword_documentation/e/eccatm/),[ECCATM (3D)](/docs/en/keyword_documentation/e/eccatm_3d/), [ECATFN (2D)](), [ECATFN (3D)](/docs/en/keyword_documentation/e/ecatfn_3d/)
