---
lang: sk
title: "CNTMTH (3D)"
---

# CNTMTH

|  (Inter-object data – 3D)  
---|---  
|  Last updated on : 27-09-2023  
  
* * *

CNTMTH Object1, Object2, Method, FSOption, InitFS

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number of first object |  None  
Object2 |  Object number of second object |  None  
Method |  Contact method between Object1 and Object2 = **0** Penalty contact = **1** Conforming coupling = **2** Augmented Lagrangian |  0  
FSOption |  Flow stress option = **0** Constant = **1** Average = **2** Individual |   
InitFS |  Initial flow stress |   
  
DEFINITION  
---  
CNTMTH specifies the contact method between two objects.  
  
REMARKS  
---  
Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Inter-object contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [CNTACT(2D)](/docs/sk/keyword_documentation/c/cntact/), [CNTACT (3D)](/docs/sk/keyword_documentation/c/cntact_3d/)
