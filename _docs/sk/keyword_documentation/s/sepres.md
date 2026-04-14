---
lang: sk
title: "SEPRES (2D3D)"
---

# SEPRES

|  (Inter-Object data)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

SEPRES Object1, Object2, DefType, Pressure (DefType = 1)

or

SEPRES Object1, Object2, DefType, FracStress (DefType = 2)

or

SEPRES Object1, Object2, DefType, Pressure (DefType = 3)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  1st Object Number |  None  
Object2 |  2nd Object Number |  None  
DefType |  Type of separation criterion = **1** System default value = **2** Percentage of flow stress = **3** Absolute pressure |  1  
FracStress |  Percentage of flow stress |  0.0  
Pressure |  Absolute pressure for nodal separation |  0.0  
  
DEFINITION  
---  
The SEPRES specifies the minimum separation criterion for nodes under pressure. Contacting nodes between the objects specified will be allowed to separate provided that they meet the set parameters.  
  
REMARKS  
---  
The two objects for which the separation criterion is to be applied to are set through the Object1 and Object2 values. Next, the type of separation criterion is set through DefType. Setting DefType to 1 or system default values will cause normal separation when the contacting node experiences a tensile force or pressure. A DefType of 2 will cause nodal separation when the pressure on the node is greater than a given percentage of flow stress (FracStress). Setting DefType to 3 will cause nodal separation when the pressure experienced by the node is greater than the variable Pressure. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Inter-Object Conditions: [Deformation](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Related keywords: [CNTACT (2D)](/docs/sk/keyword_documentation/c/cntact/), [CNTACT (3D)](/docs/sk/keyword_documentation/c/cntact_3d/)
