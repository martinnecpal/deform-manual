---
lang: sk
title: "ZSTR (2D)"
---

# ZSTR

|  (Object data – 2D)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

ZSTR Object, Itype, X

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Itype |  Definition Type  = 0 Disable = 1 Constant |  0  
X |  Numerical Value |  None  
  
DEFINITION  
---  
The keyword ZSTR is used for the 2-1/2-D simulation.  
  
REMARKS  
---  
To use this keyword it is assumed the strain rate in the direction (perpendicular to the plane) is known. The value can be obtained by calculating. | ![]({{ '/assets/equations/keyword_documentation/z/zstr_eq_1.jpg' | relative_url }}) |   
---|---  
  
It is equivalent to the plane strain case when the value is "0".

Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), Elastoplastic  
  
RELATED TOPICS  
---  
[Object Properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/): [Deformation](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/) Keywords: [GEOTYP](/docs/sk/keyword_documentation/g/geotyp/)
