---
lang: sk
title: "WMODEL (2D3D)"
---

# WMODEL

|  (Inter-Object Data)  
---|---  
|  Last updated on : 01-08-2014  
  
* * *

WMODEL Object1, Object2, Model, NumCoef

Coef(1), Coef(2), ...

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  **Object number of first object** |  None  
Object2 |  Object number of second object |  None  
Model  |  Tool wear model |  0  
|  = 0 None |   
|  = **1** Generalized Archard’s model |   
|  ![]({{ '/assets/equations/keyword_documentation/w/wmodel_eq_1.jpg' | relative_url }}) |   
|  = **2** Usui’s model |   
|  ![]({{ '/assets/equations/keyword_documentation/w/wmodel_eq_2.jpg' | relative_url }}) |   
NumCoef |  Number of coefficients in the model (**4** for Archard's and **2** for Usui's) |   
Coef(i) |  Coefficients |   
  
DEFINITION  
---  
WMODEL uses the pressure, sliding velocity, temperature at the tool/workpiece interface to estimate amount of tool wear. For a given tool wear model, the coefficients in the specific wear model should be either calibrated or found by experiments.  
  
REMARKS  
---  
Hardness is an input of Wear module, and it is also the output of the Hardness module. When Hardness module ([HDNOBJ](/docs/sk/keyword_documentation/h/hdnobj/)) is on, the Wear model will use the output of the Hardness module, which is stored in object state variables. When Hardness module is off, the Wear model will use the material hardness property ([HDNPHA](/docs/sk/keyword_documentation/h/hdnpha/)) of the element's material. Note that material hardness property may not be relevant to object hardness state variable, because the object hardness can be calculated entirely based on cooling time. Material hardness property ([HDNPHA](/docs/sk/keyword_documentation/h/hdnpha/)) can be defined as a function of temperature. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous)  
  
RELATED TOPICS  
---  
[Inter-Object Conditions](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/): [Tool wear model](/docs/sk/pre_processor/20_inter-object_data_definition/20_4_tool_wear/) Keywords: [HDNOBJ](/docs/sk/keyword_documentation/h/hdnobj/), [HDNPHA](/docs/sk/keyword_documentation/h/hdnpha/), [CNTACT (2D)](/docs/sk/keyword_documentation/c/cntact/), [CNTACT (3D)](/docs/sk/keyword_documentation/c/cntact_3d/)
