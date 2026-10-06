---
lang: en
title: "ECDEFN (2D)"
---

# ECDEFN

|  (Object Data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECDEFN Object, Ndata, Default

Num(1), node1(1) node2(1) BCfuncNum(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) BCfuncNum(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of edge constraint data sets |  None  
Num(i) |  ith data set |  None  
Default |  Default value of edge function number |  0  
node1(i) |  1st node defining edge i |  None  
node2(i) |  2nd node defining edge i |  None  
BCfuncNum(i) |  function type for deformation boundary constraint in ith data set |  None  
  
DEFINITION  
---  
ECDEFN specifies if the value of a deformation boundary (pressure) associated with a particular edge to be specified as a set of time/pressure data or as a user routine.  
  
REMARKS  
---  
The function type (Ftype) options are: < 0 user routine number > 0 function number (stored in BCCFNC) Note: If the user needs a constant pressure value, it is recommended to use ECPRES. Also, the user should be aware that the edge definition function shares the function structure with the nodal boundary condition function keyword ([BCCFNC]({{ '/docs/en/keyword_documentation/b/bccfnc/' | relative_url }})). Applicable object types: [Elastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Object Edge data: Deformation, [Boundary Constraints]({{ '/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }}): Pressure Keywords: [BCCFNC]({{ '/docs/en/keyword_documentation/b/bccfnc/' | relative_url }}), [ECPRES (2D)]({{ '/docs/en/keyword_documentation/e/ecpres/' | relative_url }}), [ECPRES (3D)]({{ '/docs/en/keyword_documentation/e/ecpres_3d/' | relative_url }}), [ECCDEF (2D)]({{ '/docs/en/keyword_documentation/e/eccdef/' | relative_url }}), [ECCDEF (3D)]({{ '/docs/en/keyword_documentation/e/eccdef_3d/' | relative_url }}), [LOCDEF (2D)]({{ '/docs/en/keyword_documentation/l/locdef/' | relative_url }}), [LOCDEF (3D)]({{ '/docs/en/keyword_documentation/l/locdef_3d/' | relative_url }})
