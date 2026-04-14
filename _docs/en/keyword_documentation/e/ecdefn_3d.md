---
lang: en
title: "ECDEFN (3D)"
---

# ECDEFN

|  (object data – 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

ECDEFN Object, Ndata, Default

Num(1), node1(1) node2(1) node3(1) node4(1) BCfuncNum(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) node3(Ndata) node4(Ndata) BCfuncNum(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of face constraint data sets |  None  
Num(i) |  ith data set |  None  
Default |  Default value of face function number |   
node1(i) |  1st node defining face i |  None  
node2(i) |  2nd node defining face i |  None  
node3(i) |  3rd node defining face i |   
node4(i) |  4th node defining face i |   
BCfuncNum(i) |  Function type for deformation boundary constraint in ith data set |  None  
  
DEFINITION  
---  
ECDEFN specifies if the value of a deformation boundary (pressure) associated with a particular face to be specified as a set of time/pressure data or as a user routine.  
  
REMARKS  
---  
The function type (Ftype) options are: < 0 user routine number > 0 function number (stored in BCCFNC) Note: If the user needs a constant pressure value, it is recommended to use ECPRES. Also, the user should be aware that the face definition function shares the function structure with the nodal boundary condition function keyword (BCCFNC). Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object Edge data: Deformation, [Boundary Constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): Pressure Keywords: [BCCFNC](/docs/en/keyword_documentation/b/bccfnc/), [ECPRES (2D)](/docs/en/keyword_documentation/e/ecpres/), [ECPRES (3D)](/docs/en/keyword_documentation/e/ecpres_3d/), [ECCDEF (2D)](/docs/en/keyword_documentation/e/eccdef/), [ECCDEF (3D)](/docs/en/keyword_documentation/e/eccdef_3d/), [LOCDEF (2D)](/docs/en/keyword_documentation/l/locdef/), [LOCDEF (3D)](/docs/en/keyword_documentation/l/locdef_3d/)
