---
lang: sk
title: "SEPDEN (2D)"
---

# SEPDEN

|  (Inter-Object data - 2D)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

SEPDEN Object1, Object2, Density

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  1st Object Number |  None  
Object2 |  2nd Object Number |  None  
Density |  Density criterion associated with nodal separation |  0.0  
  
DEFINITION  
---  
Defines the separation criterion of contacting nodes involving porous objects. Unless the density of the material is greater than Density, nodal separation is not considered.  
  
REMARKS  
---  
SEPDEN is used to model the behavior of porous objects which have not been fully compacted. Unless the porous (powdered) material is compacted past the given density, the volume will grow as the die moves back and the material density will decrease with the increasing volume. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Inter-Object Conditions: [Deformation](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Related keywords: [CNTACT (2D)](/docs/sk/keyword_documentation/c/cntact/), [CNTACT (3D)](/docs/sk/keyword_documentation/c/cntact_3d/)
